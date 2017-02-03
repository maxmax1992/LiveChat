from django.contrib import admin
from .models import User, Message, Channel

# @admin.register(User)
# class UserAdmin(UserAdmin):
#     pass

admin.site.register(Channel)
admin.site.register(Message)
admin.site.register(User)
