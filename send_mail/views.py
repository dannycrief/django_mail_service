import os
import time

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm, SendEmailForm
from django.contrib.auth import logout
from .models import EmailIHistory
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
import threading
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


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
    content = email.message

    print(receiver, email, content)
    if receiver and title and content:
        time.sleep(10)
        is_sent = send_mail(subject=title, message=content, from_email='step.kozbvb@icloud.com',
                            recipient_list=[receiver], fail_silently=False)
        if is_sent:
            email.send_status = True
            email.save()
            return redirect('email-send:email-history')


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
    context = {
        'history': user_history,
    }
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
        return redirect('email-send:to-send')
    else:
        form = SendEmailForm()
    return render(request, 'sendEmailConfig.html', {'form': form})
