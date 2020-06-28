from django.urls import path, include
from .views import index


app_name = 'email-send'
urlpatterns = [
    path('', index, name='index'),
]
