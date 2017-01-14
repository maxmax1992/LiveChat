from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Message(models.Model):
    date = models.DateTimeField()
    text = models.CharField(max_length=500);
    user = models.OneToOneField(User)
    channel = models.ForeignKey(Channel);
    pass
