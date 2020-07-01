from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class EmailIHistory(models.Model):
    user = models.ForeignKey(User, related_name='sender', verbose_name='User', on_delete=models.CASCADE)
    receiver = models.EmailField(max_length=255)
    title = models.CharField(max_length=255)
    message = models.TextField(max_length=500)
    date_of_create = models.DateField(auto_now=True)
    date_of_send = models.DateField(default=now())
    send_status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} - {self.receiver} - {self.title}'
