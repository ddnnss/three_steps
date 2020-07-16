# Generated by Django 2.1.4 on 2020-07-16 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_moderator',
            field=models.BooleanField(default=False, verbose_name='Модератор'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_test',
            field=models.BooleanField(default=False, verbose_name='Стажер'),
        ),
    ]
