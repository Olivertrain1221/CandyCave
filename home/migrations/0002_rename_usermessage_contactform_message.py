# Generated by Django 3.2 on 2022-07-30 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='usermessage',
            new_name='message',
        ),
    ]
