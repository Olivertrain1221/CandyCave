# Generated by Django 3.2 on 2022-07-21 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20220721_1500'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderlineitem',
            old_name='sweet_size',
            new_name='measurement_of_sweet',
        ),
    ]
