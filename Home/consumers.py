# In consumers.py
from channels import Group
from channels.auth import channel_session_user_from_http
import json
from .models import ChannelParticipant, Channel, User, Message
from channels.sessions import channel_session

# Connected to websocket.connect
@channel_session_user_from_http
def ws_connect(message):
    # Accept connection
    message.reply_channel.send({"accept": True})
    # Work out room name from path (ignore slashes)
    # room = message.content['path'].strip("/").split("/")
    # r = message.content['path'].split("/")[2];
    room = message.content['path'].split("/")[2];

    # Save room in session and add us to the group
    # add user to the channel if its not in the group
    message.channel_session['room'] = room
    Group("chat-%s" % room).add(message.reply_channel)

# Connected to websocket.receive
@channel_session_user_from_http
def ws_message(message):
    room = message.channel_session['room']
    obj = json.loads(message['text'])

    channel = Channel.objects.get(pk=room)

    username = obj['username']
    msg = obj['message']
    user = User.objects.get(username=username)
    participant = ChannelParticipant.objects.get(user=user)

    # print(message.channel_session['room'])
    messageobj = Message.objects.create(user=participant, text=msg, chat=channel)
    messageobj.save()
    # print(message.user.get_username())

    Group("chat-%s" % room).send({
        "text": message['text'],
    })

# Connected to websocket.disconnect
@channel_session_user_from_http
def ws_disconnect(message):
    Group("chat-%s" % message.channel_session['room']).discard(message.reply_channel)
