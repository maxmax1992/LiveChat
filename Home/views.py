from django.shortcuts import render
from .models import User, Message, Channel
from django.contrib.auth import authenticate, login



# currently returns dummy index with all users listed.
def channels(request):
    channels = Channel.objects.all()
    return render(request, 'Home/index.html', {'channels': channels})



def userDetail(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'Home/userDetail.html', {'user': user})


def channelDetail(request, channel_id):
    channel = Channel.objects.get(id=channel_id)
    return render(request, 'Home/channelDetail.html', {'channel': channel})



def loginView(request):
    return render(request, 'Home/login.html')


def loginApprove(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return render(request, 'Home/logged_in.html')
    else:
        return render(request, 'Home/loggin_fail.html')
        # Return an 'invalid login' error message.