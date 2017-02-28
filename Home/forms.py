from django import forms
from django.forms import RadioSelect
from .models import Channel

class ChannelForm(forms.ModelForm):

    class Meta:
        model = Channel
        fields = ['name'];