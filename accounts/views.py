from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from users.models import Profile
from users import form as uform
from django.contrib.auth import get_user_model
# Create your views here.


def signup_view(request):
    messages={}
    if request.method == 'POST':
        image = request.POST.get('img')
        first_name = request.POST.get('first')
        second_name = request.POST.get('second')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        bio = request.POST.get('bio')

        if len(password1) < 8:
            messages['Password must be at least 8 characters with letters, numbers and at least one symbol']='Invalid'

        elif password1 == password2:
            user = User.objects.create_user(username, email, password1,
                                            first_name=first_name,
                                            last_name=second_name,)

            profile = Profile(image=image, gender=gender,
                              intro=bio, user=user)

            profile.save()

            login(request, user)

            return redirect('articles:list')
    
        else:
            messages['passwords do not match'] = 'passwords do not match'

    return render(request, 'accounts/signup_view.html', {'messages': messages})


def login_view(request):
    messages={}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')

        else:
            messages['Username/Password is incorrect'] = 'Username/Password is incorrect'
            return render(request, 'accounts/signup_view.html', {'messages': messages})

    else:
        return redirect('accounts:signup')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')
