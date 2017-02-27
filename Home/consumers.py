# In consumers.py
from channels import Group
from channels.auth import channel_session_user_from_http
from .models import ChannelParticipant, Channel
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
    print(message['text'])
    Group("chat-%s" % message.channel_session['room']).send({
        "text": message['text'],
    })

# Connected to websocket.disconnect
@channel_session_user_from_http
def ws_disconnect(message):
    Group("chat-%s" % message.channel_session['room']).discard(message.reply_channel)
