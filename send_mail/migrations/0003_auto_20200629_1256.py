# Generated by Django 3.0.7 on 2020-06-29 12:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('send_mail', '0002_auto_20200629_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailihistory',
            name='date_of_send',
            field=models.DateField(default=datetime.datetime(2020, 6, 29, 12, 56, 29, 74595, tzinfo=utc)),
        ),
    ]
