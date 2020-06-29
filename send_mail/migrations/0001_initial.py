# Generated by Django 3.0.7 on 2020-06-29 12:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailIHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.EmailField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('message', models.TextField(max_length=500)),
                ('date_of_create', models.DateField(auto_now=True)),
                ('date_of_send', models.DateField(default=datetime.datetime(2020, 6, 29, 12, 39, 3, 434568, tzinfo=utc))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL, verbose_name='Sender')),
            ],
        ),
    ]
