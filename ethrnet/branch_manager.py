from django.db import models
from django.contrib.auth.models import AnonymousUser

class BranchWiseObjectManager(models.Manager):

    def all(self, user):
        print user
        if user.is_anonymous():
            return super(BranchWiseObjectManager, self).get_queryset()
        if user.is_staff:
            return super(BranchWiseObjectManager, self).get_queryset()
        return super(BranchWiseObjectManager, self).get_queryset().filter(branch=user.userprofile.branch)
