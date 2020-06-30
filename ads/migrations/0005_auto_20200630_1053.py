# Generated by Django 2.2.7 on 2020-06-30 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_auto_20200630_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='action_type',
            field=models.CharField(choices=[('TR', 'Сдать'), ('SL', 'Продать'), ('BY', 'Купить'), ('RT', 'Снять')], default='TR', max_length=20, verbose_name='Тип сделки'),
        ),
        migrations.AlterField(
            model_name='ads',
            name='balkon_type',
            field=models.CharField(blank=True, choices=[('B', 'Балкон'), ('L', 'Лоджия'), ('BB', '2 балкона'), ('L', '2 лоджии')], max_length=20, null=True, verbose_name='Балкон'),
        ),
        migrations.AlterField(
            model_name='ads',
            name='currency_type',
            field=models.CharField(choices=[('RU', 'Рубли'), ('US', 'Доллары')], default='RU', max_length=20, verbose_name='Валюта'),
        ),
        migrations.AlterField(
            model_name='ads',
            name='house_type',
            field=models.CharField(blank=True, choices=[('BR', 'Кирпич'), ('MN', 'Монолит'), ('PL', 'Панель')], max_length=20, null=True, verbose_name='Тип постройки'),
        ),
        migrations.AlterField(
            model_name='ads',
            name='land_type',
            field=models.CharField(blank=True, choices=[('IG', 'ИЖС'), ('SN', 'СНТ (ДНП)'), ('LP', 'ЛПХ'), ('PR', 'Промназначения')], max_length=20, null=True, verbose_name='Категория земель'),
        ),
        migrations.AlterField(
            model_name='ads',
            name='order_type',
            field=models.CharField(blank=True, choices=[('FS', 'Свободная продажа'), ('AL', 'Альтернатива'), ('CH', 'Обмен'), ('FR', 'Свободна')], max_length=20, null=True, verbose_name='Тип сделки'),
        ),
        migrations.AlterField(
            model_name='ads',
            name='own_years',
            field=models.CharField(blank=True, choices=[('IG', 'Менее 3х лет'), ('SN', 'Более 3х лет'), ('LP', 'Более 5х лет')], max_length=20, null=True, verbose_name='Лет в собственности'),
        ),
        migrations.AlterField(
            model_name='ads',
            name='rooms',
            field=models.CharField(blank=True, choices=[('R1', '1'), ('R2', '2'), ('R3', '3'), ('R4', '4'), ('R5', '5+')], max_length=20, null=True, verbose_name='Комнат'),
        ),
    ]