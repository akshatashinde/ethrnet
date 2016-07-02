from enum import Enum

from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from django_resized import ResizedImageField

from user_auth.models import User


class Branch(models.Model):
    name = models.CharField(max_length=120,)
    code = models.CharField(max_length=120,)
    pincodes = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class UserAddress(models.Model):
    address = models.CharField(max_length=120,)
    flat_no = models.CharField(max_length=120,)
    society = models.CharField(max_length=120,)
    area = models.ForeignKey(Branch, null=True, blank=True)
    city = models.CharField(max_length=120, default="Pune")
    state = models.CharField(max_length=120, null=True, blank=True, default="Maharashtra")
    country = models.CharField(max_length=120,default="India", null=True, blank=True)
    zipcode = models.CharField(max_length=25)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    get_latest_by = "timestamp"

    def __unicode__(self):
        return self.get_address()

    def get_address(self):
        address = ""
        if self.flat_no:
            address += "Flat No. " + self.flat_no
        if self.society:
            address += " " + self.society + ",<br/>"
        else:
            address += "<br/>"
        if self.area:
            address += self.area.name
        if self.city:
            address += " ," + self.city + ",<br/>"
        else:
            address += "<br/>"
        if self.state:
            address += self.state
        if self.country:
            address += " ," + self.country + ",<br/>"
        else:
            address += "<br/>"
        if self.zipcode:
            address += "Pincode - " +self.zipcode
        return address

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
        NORMAL_USER = 'Normal User'

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
    branch = models.ForeignKey(Branch, null=True, blank=True)
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

    def __unicode__(self):
        return u''.join((self.first_name, self.last_name))

@receiver(post_save, sender=User)
def create_profile_for_user(sender, instance=None,
                            created=False, **kwargs):
    """
    When a new user is created this fuctions creates a userprofile
    and associates it with the newly created user.
    """
    if created:
            UserProfile.objects.create(
                user=instance)


@receiver(pre_delete, sender=User)
def delete_profile_for_user(sender, instance=None, **kwargs):
    """
    When a user is deleted this fuctions deletes the userprofile
    of that particular user.
    """
    if instance:
            user_profile = UserProfile.objects.get(user=instance)
            user_profile.delete()
