 # -*- coding: utf-8 -*-

from django.contrib.auth.models import AbstractUser
"""
class User(AbstractUser):
    phone = models.CharField(max_length=12)
    city = models.CharField(max_length=200)

    def __unicode__(self):
        return self.username
"""

class User(AbstractUser):

    objects = None # we cannot really use this w/o local DB

    username = "my_user"  # and all the other properties likewise.
                   # They're defined as model.CharField or similar,
                   # and we can't allow that

    def get_full_name(self):
        # The user is identified by their email address
        return self.username

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def is_staff(self):
        return True

    def is_active(self):
        return True

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def save (self, **kwargs):
        """saving to DB disabled"""
        pass

    def get_full_name(self):
        return 'my_user'

    def get_group_permissions (self):
        """If you don't make your own permissions module,
           the default also will use the DB."""
        return [] # likewise with the other permission defs

    def get_and_delete_messages (self):
        """Messages are stored in the DB."""
        return []
