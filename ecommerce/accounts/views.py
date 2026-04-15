from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User


def register(request):
    if request.user.is_authenticated:
        return redirect('store:home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Save extra fields
            user.first_name = request.POST.get('first_name', '')
            user.last_name = request.POST.get('last_name', '')
            user.email = request.POST.get('email', '')
            user.save()
            login(request, user)
            messages.success(request, f'Welcome, {user.username}! Your account has been created.')
            return redirect('store:home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('store:home')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            next_url = request.GET.get('next', 'store:home')
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('store:home')


@login_required
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', '')
        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('accounts:profile')
    return render(request, 'accounts/profile.html', {'user': request.user})
