# Generated by Django 3.2 on 2022-08-01 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='slug',
            field=models.SlugField(default=1, max_length=128, unique=True),
            preserve_default=False,
        ),
    ]
