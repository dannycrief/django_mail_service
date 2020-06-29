import time

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm, SendEmailForm
from django.contrib.auth import logout
from .models import EmailIHistory
from django.core.mail import send_mail
import threading


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
        return redirect('email-send:index')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('email-send:index')


@login_required
def send_letter(email):
    receiver = email.receiver
    title = email.title
    message = email.message
    print(receiver, email, message)
    if receiver and title and message:
        time.sleep(10)
        email.send_status = True
        email.save()
        send_mail(title, message, None, [receiver], fail_silently=False)


@login_required
def to_send(request):
    threads = []
    user_history = EmailIHistory.objects.filter(send_status=False, user_id=request.user.id)
    for email in user_history:
        if request.method == "POST":
            t = threading.Thread(target=send_letter, args=(email,))
            threads.append(t)
            print('Starting')
            t.start()

    for t in threads:
        print('ENDING')
        t.join()
    context = {'history': user_history}
    return render(request, 'toSend.html', context)


@login_required
def history(request):
    user_history = EmailIHistory.objects.filter(user_id=request.user.id)
    context = {'history': user_history}
    return render(request, 'history.html', context)


@login_required
def send_email(request):
    if request.method == "POST":
        form = SendEmailForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('email-send:email-history')
    else:
        form = SendEmailForm()
    return render(request, 'sendEmailConfig.html', {'form': form})
