from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as auth_logout

from .forms import CustomUserCreationForm
from .models import User

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            auth_login(request, user)
            return redirect('community:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/form.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('community:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/form.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('community:index')

@login_required
def profile(request, username):
    User = get_user_model()
    user = get_object_or_404(User, username=username)
    context = {
        'user':user
    }
    return render(request, 'accounts/profile.html', context)

def follow(request, username):
    # bringing the data
    User = get_user_model()
    # the person getting followed
    user = get_object_or_404(User, username=username)
    # the owner of the profile => user
    # the person asking to follow => request.user
    if user != request.user:
        if user.followers.filter(username=request.user.username).exists():
            user.followers.remove(request.user)
        else:
            user.followers.add(request.user)
    return redirect('accounts:profile', user.username)

def follow_list(request, username):
    User = get_user_model()
    user = get_object_or_404(User, username=username)
    # GET method
    if request.GET.get('list') == 'followers':
        f_list = user.followers.all()
        follow_name = 'followers'
    elif request.GET.get('list') == 'followings':
        f_list = user.followings.all()
        follow_name = 'followings'
    context = {
        'user':user,
        'f_list':f_list,
    }
    return render(request, 'accounts/follow_list.html', context)