# Generated by Django 4.1.3 on 2022-11-09 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_message_read'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='read',
        ),
    ]
