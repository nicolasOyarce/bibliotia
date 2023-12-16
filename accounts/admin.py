from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

from .models import Account, UserProfile


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_admin', 'last_login')
    readonly_fields = ('created', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        """
        Display thumbnail of the profile picture in the admin panel
        """
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
    thumbnail.short_description = 'Profile Picture'
    list_display = ('thumbnail', 'user', 'city', 'comuna')

admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
