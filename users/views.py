from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login



def CreateUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, Your Account is Created')
            return redirect('users:login')
    else:
        form = UserForm()
    return render(request, 'users/registration.html',{'form':form})


def Login(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            if username != "" and User.objects.filter(username=username).exists():

                user = authenticate(request, username=username, password= password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
                else:
                    messages.info(request,'Password Invalid!')
                    return redirect('users:login')
            else:
                messages.info(request,'Username is invalid')
                return redirect('users:login')
    return render(request,'users/login.html',{'form':form})
            