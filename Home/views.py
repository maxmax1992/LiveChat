from django.shortcuts import render, redirect
from itertools import chain
from Home.forms import ChannelForm
from .models import User, Message, Channel, ChannelParticipant
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.timezone import get_current_timezone


# currently returns dummy index with all users listed.
@login_required(login_url='/login/')
def channels(request):

    channels = Channel.objects.all()
    return render(request, 'Home/index.html', {'channels': channels})


# TODO
@login_required(login_url='/login/')
def userDetail(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'Home/userDetail.html', {'user': user})


@login_required(login_url='/login/')
def channelDetail(request, channel_id):
    channel = Channel.objects.get(id=channel_id)
    print(request.user.is_authenticated)

    try:
        participant = ChannelParticipant.objects.get(user=request.user)
    except ChannelParticipant.DoesNotExist:
        participant = None

    if participant is None:
        participant = ChannelParticipant.objects.create(user=request.user, channel=channel)
        participant.save()

    # check if user is a participant or not,
    # if not add channelParticipant to database
    users = channel.users
    messages = reversed(channel.messages.order_by('-created_at')[:50])

    return render(request, 'Home/channelDetail.html',
                  {'channel': channel, 'messages': messages, 'users': users, 'theuser': participant})


def loginView(request):
    if request.method == 'POST':
        if "loginButton" in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return redirect('/')
            else:
                return render(request, 'Home/login.html', {'error_message': "Invalid email or password"})
        else:
            data = {}

            username = request.POST['username']
            password = request.POST['password']
            password2 = request.POST['password2']
            email = request.POST['email']
            # developer = request.POST.get['developer', False]
            try:
                User.objects.get(username=username)
                data.update({"username_error": "This username already exists"})
            except:
                pass
            try:
                User.objects.get(email=email)
                data.update({"email_error": "This email already exists"})
            except:
                pass
            if password != password2:
                data.update({"password_error": "The passwords did not match"})
            # password = request.POST['password']

            if len(data) > 0:
                data["tab2"] = "tab2"
                return render(request, 'Home/login.html', data)
            else:
                user = User.objects.create(username=username, password=password, email=email);
                if request.POST.get('developer', False):
                    user.isDeveloper = True
                user.set_password(user.password)
                user.save()
                login(request, user)
                return redirect('/')

                # Return an 'invalid login' error message.
    else:
        return render(request, 'Home/login.html')


@login_required(redirect_field_name='index')
def logOut(request):
    logout(request)
    return redirect('about')

def about(request):
    return render(request, 'Home/about.html')


@login_required(redirect_field_name='login')
def createChannel(request):
    if request.method == 'POST':
        form = ChannelForm(request.POST or None)
        if form.is_valid():
            channel = form.save(commit=False)
            channel.creator = request.user
            radioVal = request.POST['optionsRadios']
            if radioVal == 'option2':
                channel.isPrivate = True
            channel.save()
            return redirect('/')
        context = {
            "form": form
        }
        return render(request, 'games/createChannel.html', context)
    else:
        return render(request, 'Home/createChannel.html')
