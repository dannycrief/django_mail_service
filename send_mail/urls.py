from django.urls import path, include
from .views import index, to_send, send_email, history

app_name = 'email-send'
urlpatterns = [
    path('', index, name='index'),
    path('tosend/', to_send, name='to-send'),
    path('history/', history, name='email-history'),
    path('sendemail/', send_email, name='send-email'),
]
