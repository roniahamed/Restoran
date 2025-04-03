from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib import messages
from django.contrib.



def CreateUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, Your Account is Created')
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'users/registration.html',{'form':form})


def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            