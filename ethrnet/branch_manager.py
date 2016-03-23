from django.db import models


class BranchWiseObjectManager(models.Manager):
    def all(self, user):
        if user.is_staff:
            return super(BranchWiseObjectManager, self).get_queryset()
        return super(BranchWiseObjectManager, self).get_queryset().filter(branch=user.userprofile.branch)

