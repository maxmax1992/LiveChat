from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
import datetime
from django.db import models


class User(AbstractUser, models.Model):
    email = models.EmailField(
        _('Email Address'), unique=True,
        error_messages={
            'unique': _("A user with that email already exists."),
        }
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    isDeveloper = models.BooleanField(default=False)
    def __str__(self):
        string = ""
        string += "Username: " + self.username + " mail: " + self.email
        return string

    #
    # def get_username(self):
    #     return self.email
    '''
    Scenario 1
     Create 2 users
     User1 creates 1 channel 1
     User2 joins channel 1
     User1 posts message to chat
     User2 posts message to chat

     channel must have 2 messages from
     User1,
     User2

     all sorted by date
    '''

class ChannelParticipant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey('Channel', on_delete=models.CASCADE, related_name='users')
    isBanned = models.BooleanField(default=False)


class Channel(models.Model):
    name = models.CharField(max_length=100, default='')
    creator = models.ForeignKey(User)
    isPrivate = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Message(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(Channel, on_delete=models.CASCADE, default=1, related_name='messages')
    text = models.CharField(max_length=500)
    user = models.ForeignKey(ChannelParticipant, on_delete=models.CASCADE, related_name='messages')

    class Meta:
        ordering = ['created_at']

    def getTime(self):
        return int(self.created_at.strftime("%s"))*1000

    def __str__(self):
        return "Message : {} \n by user {}" .format(self.text, self.user)


