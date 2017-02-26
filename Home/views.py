from django.shortcuts import render, redirect
from .models import User, Message, Channel
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.timezone import get_current_timezone



# currently returns dummy index with all users listed.
def channels(request):
    channels = Channel.objects.all()
    return render(request, 'Home/index.html', {'channels': channels})



def userDetail(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'Home/userDetail.html', {'user': user})


@login_required(login_url='/login/')
def channelDetail(request, channel_id):
    tz = get_current_timezone()
    channel = Channel.objects.get(id=channel_id)

    # users = User.objects.all()
    users = channel.users
    messages = reversed(channel.messages.order_by('-created_at')[:50])
    user = request.user
    return render(request, 'Home/channelDetail.html',
                  {'channel': channel,'messages': messages, 'users': users, 'user': user})



def loginView(request):
    if request.method == 'POST':
        if "loginButton" in request.POST:
            print("loginButtoooooon")
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
                User.objects.get(username = username)
                data.update({"username_error": "This username already exists"})
            except:
                pass
            try:
                User.objects.get(email = email)
                data.update({"email_error": "This email already exists"})
            except:
                pass
            if password != password2:
                data.update({"password_error": "The passwords did not match"})
            #     password = request.POST['password']

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
    return render(request, 'Home/index.html')




















