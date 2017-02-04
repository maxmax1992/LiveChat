from django.contrib import admin
from .models import User, Message, Channel, ChannelParticipant

# @admin.register(User)
# class UserAdmin(UserAdmin):
#     pass

admin.site.register(Channel)
admin.site.register(Message)
admin.site.register(User)
admin.site.register(ChannelParticipant)
