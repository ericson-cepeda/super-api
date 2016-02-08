from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext, ugettext_lazy as _
"""
from application.accounts.models import User

from application.accounts import forms

class UserAdmin(UserAdmin):

    add_form = forms.UserCreationAdminForm

    list_display = ('__unicode__', 'is_staff',
                  )

    fieldsets = (
                (None, {'fields': ('username')}),
                (_('Personal info'), {'fields': ('is_superuser')}),
              )


admin.site.register(User, UserAdmin)
"""