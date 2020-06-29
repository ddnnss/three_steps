# Generated by Django 2.1.4 on 2020-06-29 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, editable=False, max_length=255, null=True, verbose_name='Номер объекта')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Заголовок')),
                ('is_new_building', models.BooleanField(default=False, verbose_name='Новострой ?')),
                ('is_checked', models.BooleanField(default=False, verbose_name='Проверено ?')),
                ('is_publish', models.BooleanField(default=False, verbose_name='Опубликован ?')),
                ('is_hot', models.BooleanField(default=False, verbose_name='Горячие предложения ?')),
                ('is_in_ya_feed', models.BooleanField(default=False, verbose_name='Выгружать в Яндекс фид ?')),
                ('action_type', models.CharField(choices=[('TR', 'Сдать'), ('SL', 'Продать'), ('BY', 'Купить'), ('RT', 'Снять')], default='TR', max_length=2, verbose_name='Тип')),
                ('street', models.CharField(max_length=255, null=True, verbose_name='Улица')),
                ('street_number', models.CharField(max_length=255, null=True, verbose_name='Номер дома')),
                ('room_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='Номер квартиры')),
                ('cadaster_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='Кадастровый номер')),
                ('floor', models.IntegerField(blank=True, null=True, verbose_name='Этаж')),
                ('floor_total', models.IntegerField(blank=True, null=True, verbose_name='Этажность')),
                ('house_type', models.CharField(blank=True, choices=[('BR', 'Кирпич'), ('MN', 'Монолит'), ('PL', 'Панель')], max_length=2, null=True, verbose_name='Тип')),
                ('rooms', models.CharField(blank=True, choices=[('R1', '1'), ('R2', '2'), ('R3', '3'), ('R4', '4'), ('R5', '5+')], max_length=2, null=True, verbose_name='Комнат')),
                ('balkon_type', models.CharField(blank=True, choices=[('B', 'Балкон'), ('L', 'Лоджия'), ('BB', '2 балкона'), ('L', '2 лоджии')], max_length=2, null=True, verbose_name='Балкон')),
                ('square_total', models.IntegerField(blank=True, null=True, verbose_name='Площадь общая')),
                ('square_living', models.IntegerField(blank=True, null=True, verbose_name='Площадь жилая')),
                ('square_kitchen', models.IntegerField(blank=True, null=True, verbose_name='Площадь кухни')),
                ('square_room', models.IntegerField(blank=True, null=True, verbose_name='Площадь комнаты')),
                ('square_land', models.IntegerField(blank=True, null=True, verbose_name='Площадь земли')),
                ('land_type', models.CharField(blank=True, choices=[('IG', 'ИЖС'), ('SN', 'СНТ (ДНП)'), ('LP', 'ЛПХ'), ('PR', 'Промназначения')], max_length=2, null=True, verbose_name='Категория земель')),
                ('order_type', models.CharField(blank=True, choices=[('FS', 'Свободная продажа'), ('AL', 'Альтернатива'), ('CH', 'Обмен'), ('FR', 'Свободна')], max_length=2, null=True, verbose_name='Тип сделки')),
                ('own_years', models.CharField(blank=True, choices=[('IG', 'Менее 3х лет'), ('SN', 'Более 3х лет'), ('LP', 'Более 5х лет')], max_length=2, null=True, verbose_name='Лет в собственности')),
                ('contact_name', models.CharField(max_length=255, null=True, verbose_name='Контактное лицо (собственник)')),
                ('contact_phone', models.CharField(max_length=255, null=True, verbose_name='Телефон (собственник)')),
                ('contact_email', models.CharField(blank=True, max_length=255, null=True, verbose_name='Email (собственник)')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('currency_type', models.CharField(choices=[('RU', 'Рубли'), ('US', 'Доллары')], default='RU', max_length=2, verbose_name='Тип')),
                ('price', models.IntegerField(null=True, verbose_name='Цена')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Изменено')),
            ],
            options={
                'verbose_name': 'Обьявление',
                'verbose_name_plural': 'Обьявления',
            },
        ),
        migrations.CreateModel(
            name='AdsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='ads/image', verbose_name='Изображение')),
                ('image_thumb', models.ImageField(blank=True, editable=False, null=True, upload_to='ads/image', verbose_name='Изображение')),
                ('image_main', models.ImageField(blank=True, editable=False, null=True, upload_to='ads/image', verbose_name='Изображение')),
                ('ads', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ads.Ads', verbose_name='Для обьявления')),
            ],
            options={
                'verbose_name': 'Фото для объявления',
                'verbose_name_plural': 'Фото для объявлений',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Категория')),
                ('name_slug', models.CharField(blank=True, editable=False, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Metro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Метро')),
                ('name_slug', models.CharField(blank=True, editable=False, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Метро',
                'verbose_name_plural': 'Метро',
            },
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Город')),
                ('name_slug', models.CharField(blank=True, editable=False, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.AddField(
            model_name='ads',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ads.Category', verbose_name='Категория'),
        ),
    ]