from enum import Enum

from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from django_resized import ResizedImageField

from user_auth.models import User


class UserAddress(models.Model):
    address = models.CharField(max_length=120,)
    flat_no = models.CharField(max_length=120,)
    society = models.CharField(max_length=120,)
    area = models.CharField(max_length=120,)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120, null=True, blank=True)
    country = models.CharField(max_length=120,default="India")
    zipcode = models.CharField(max_length=25)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    get_latest_by = "timestamp"

    def __unicode__(self):
        return self.get_address()

    def get_address(self):
        return "%s,<br/>%s - %s.<br/>%s, %s." %(self.address, self.zipcode, self.city, self.state, self.country)

    class Meta:
        ordering = ['-updated', '-timestamp']


class UserProfile(models.Model):

    """
    This class creates attributes userprofile.
    """
    class UserTypes(Enum):
        """
        This class creates enum for user_type field of UserProfile.
        """
        ADMINISTRATOR = 'Administrator'
        MASTER = 'Master'
        UI_MASTER = 'UI Master'
        MARKETING_MASTER = 'Marketing Master'
        DISPATCHER_MASTER = 'Dispatcher Master'
        NORMAL_USER = 'Normal User'

        @classmethod
        def as_tuple(cls):
            return ((item.value, item.name.replace('_', ' ')) for item in cls)

    class Gender(Enum):
        """
        This class creates enum for gender field of UserProfile.
        """
        MALE = 'Male'
        FEMALE = 'Female'

        @classmethod
        def as_tuple(cls):
            return ((item.value, item.name.replace('_', ' ')) for item in cls)

    user = models.OneToOneField(User, primary_key=True)
    first_name = models.CharField(blank=True, max_length=50)
    last_name = models.CharField(blank=True, max_length=50)
    user_type = models.CharField(blank=True, max_length=50,
                                 choices=UserTypes.as_tuple(),
                                 default=UserTypes.NORMAL_USER.value
                                 )
    mobile_no = models.CharField(blank=True, max_length=10)
    gender = models.CharField(blank=True, max_length=20,
                              choices=Gender.as_tuple())
    dob = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to='profile_picture/',
        blank=True,
        null=True
    )
    profile_picture_icon = ResizedImageField(
        size=[20, 20],
        quality=100,
        crop=['middle', 'center'],
        upload_to='profile_picture/',
        blank=True,
        null=True
    )
    profile_picture_thumbnail = ResizedImageField(
        size=[300, 200],
        quality=100,
        upload_to='profile_picture/',
        blank=True,
        null=True
    )
    addresses = models.ManyToManyField(UserAddress)

    def __unicode__(self):
        return u''.join((self.first_name, self.last_name))

    @property
    def address(self):
        return self.addresses.latest(field_name="timestamp")

    @receiver(post_save, sender=User)
    def create_profile_for_user(sender, instance=None,
                                created=False, **kwargs):
        """
        When a new user is created this fuctions creates a userprofile
        for that particular user.
        """
        if created:
            UserProfile.objects.create(user=instance)

        if instance.is_staff:
            instance.userprofile.user_type = UserProfile.UserTypes.ADMINISTRATOR.value
            instance.userprofile.save()

    @receiver(pre_delete, sender=User)
    def delete_profile_for_user(sender, instance=None, **kwargs):
        """
        When a user is deleted this fuctions deletes the userprofile
        of that particular user.
        """
        if instance:
            user_profile = UserProfile.objects.get(user=instance)
            user_profile.delete()
