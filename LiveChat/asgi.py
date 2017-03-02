import os
import channels.asgi
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LiveChat.settings")
channel_layer = channels.asgi.get_channel_layer()
application = DjangoWhiteNoise(channel_layer)
