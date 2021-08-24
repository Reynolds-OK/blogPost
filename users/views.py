from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User as Us
from django.contrib.auth.hashers import check_password
from .models import Profile
from articles.models import Article



def user_profile(request, username, id):
    us = Us.objects.get(username=username)
    articles = Article.objects.filter(author=id)
    profile = Profile.objects.get(user=id)
    if request.method == 'POST':
        profile.image = request.FILES.get('img', profile.image.name)
        profile.intro = request.POST.get('intro', None)
        profile.gender = request.POST.get('gender', None)  
        profile.save()

        us.first_name = request.POST.get('first', None)
        us.last_name = request.POST.get('second', None)
        us.username = request.POST.get('username', None)
        us.email = request.POST.get('email', None)
        us.save()

    context = {'user':us, 'articles':articles, 'profile':profile}
    return render(request, 'profiles/user_profile.html', context)


def password(request, id):
    messages ={}
    user = Us.objects.get(id=id)
    if request.method == 'POST':
        old = request.POST.get('old')
        new = request.POST.get('new')
        second = request.POST.get('second')

        if check_password(old, user.password):
            if new == second:
                user.set_password(new)
                user.save()
                messages['Password changed successfully'] = 'Password changed'
            else:
                messages['Passwords do not match'] = 'Passwords do not match'
        else:
            messages['Password does not exist']='password does not exist'

    return render(request, 'profiles/password.html', {'user':user, 'messages': messages})
