from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import logout


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('email-send:index')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('email-send:index')
