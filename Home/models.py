from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser, models.Model):
    isDeveloper = models.BooleanField(default=False)


    def __str__(self):
        string = ""
        string += "Username: " + self.username + " mail: " + self.email
        return string


class Channel(models.Model):
    name = models.CharField(max_length=100, default='')
    creator = models.ForeignKey(User)

    def __str__(self):
        return self.name


class Message(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    chat = models.ForeignKey(Channel, on_delete=models.CASCADE, default=1)
    text = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Message : {} \n by user {}" .format(self.text, self.user)


