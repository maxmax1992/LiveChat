from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Message, Channel

# @admin.register(User)
# class UserAdmin(UserAdmin):
#     pass

admin.site.register(Channel)
admin.site.register(Message)
admin.site.register(User)
