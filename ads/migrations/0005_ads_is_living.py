# Generated by Django 2.1.4 on 2020-07-23 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_auto_20200716_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='is_living',
            field=models.BooleanField(default=True, verbose_name='Жилая? (Для фида)'),
        ),
    ]
