# Generated by Django 3.2 on 2022-07-07 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sweets', '0004_auto_20220701_1305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sweet',
            old_name='has_sizes',
            new_name='measurement_of_sweet',
        ),
    ]
