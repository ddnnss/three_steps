from django.db import models
from customuser.models import User
from pytils.translit import slugify
from django.db.models.signals import post_save
from django.core.files import File
from io import BytesIO
from pytils.translit import slugify
from PIL import Image

class Metro(models.Model):
    name = models.CharField('Метро', max_length=255, blank=False, null=True)
    name_slug = models.CharField(blank=True, max_length=255, null=True, editable=False)

    def save(self, *args, **kwargs):
        #создание имени для ЧПУ ссылки
        self.name_slug = slugify(self.name)
        super(Metro, self).save(*args, **kwargs)

    def __str__(self):
        return f'Метро : {self.name} '

    class Meta:
        verbose_name = "Метро"
        verbose_name_plural = "Метро"

class Category(models.Model):
    name = models.CharField('Категория', max_length=255, blank=False, null=True)
    name_slug = models.CharField(blank=True, max_length=255, null=True, editable=False)

    def save(self, *args, **kwargs):
        #создание имени для ЧПУ ссылки
        self.name_slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return f'Категория : {self.name} '

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Town(models.Model):
    name = models.CharField('Город', max_length=255, blank=False, null=True)
    name_slug = models.CharField(blank=True, max_length=255, null=True, editable=False)

    def save(self, *args, **kwargs):
        # создание имени для ЧПУ ссылки
        self.name_slug = slugify(self.name)
        super(Town, self).save(*args, **kwargs)

    def __str__(self):
        return f'Город : {self.name} '

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

class Ads(models.Model):
    TO_RENT = 'TR'
    SELL = 'SL'
    BUY = 'BY'
    RENT = 'RT'
    ACTION_TYPE_CHOICES = [
        (TO_RENT, 'Сдать'),
        (SELL, 'Продать'),
        (BUY, 'Купить'),
        (RENT, 'Снять'),
    ]

    BRICK = 'BR'
    MONOLITH = 'MN'
    PANEL = 'PL'
    HOUSE_TYPE_CHOICES = [
        (BRICK, 'Кирпич'),
        (MONOLITH, 'Монолит'),
        (PANEL, 'Панель'),
    ]

    R1 = 'R1'
    R2 = 'R2'
    R3 = 'R3'
    R4 = 'R4'
    R5 = 'R5'
    ROOMS_NUMBER_CHOICES = [
        (R1, '1'),
        (R2, '2'),
        (R3, '3'),
        (R4, '4'),
        (R5, '5+'),
    ]

    BALKON = 'B'
    LODGIA = 'L'
    BALKON2 = 'BB'
    LODGIA2 = 'LL'
    BALKON_TYPE_CHOICES = [
        (BALKON, 'Балкон'),
        (LODGIA, 'Лоджия'),
        (BALKON2, '2 балкона'),
        (LODGIA, '2 лоджии'),
    ]

    IGS = 'IG'
    SNT = 'SN'
    LPH = 'LP'
    PROM = 'PR'
    LAND_TYPE_CHOICES = [
        (IGS, 'ИЖС'),
        (SNT, 'СНТ (ДНП)'),
        (LPH, 'ЛПХ'),
        (PROM, 'Промназначения'),
    ]

    FREE_SALE = 'FS'
    ALTERNATIVE = 'AL'
    CHANGE = 'CH'
    FREE = 'FR'
    ORDER_TYPE_CHOICES = [
        (FREE_SALE, 'Свободная продажа'),
        (ALTERNATIVE, 'Альтернатива'),
        (CHANGE, 'Обмен'),
        (FREE, 'Свободна'),
    ]

    L3 = 'IG'
    G3 = 'SN'
    G5 = 'LP'
    OWN_YEARS_CHOICES = [
        (L3, 'Менее 3х лет'),
        (G3, 'Более 3х лет'),
        (G5, 'Более 5х лет'),
    ]

    RUB = 'RU'
    USD = 'US'
    CURRENCY_CHOICES = [
        (RUB, 'Рубли'),
        (USD, 'Доллары'),
    ]

    created = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Добавил')
    number = models.CharField('Номер объекта', max_length=255, blank=True, null=True, editable=False)
    name = models.CharField('Заголовок', blank=False, max_length=255, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=True,verbose_name='Категория')
    metro = models.ForeignKey(Metro, on_delete=models.CASCADE, blank=True, null=True,verbose_name='Метро')
    is_new_building = models.BooleanField('Новострой ?', default=False)
    is_checked = models.BooleanField('Проверено ?', default=False)
    is_publish = models.BooleanField('Опубликован ?', default=False)
    is_hot = models.BooleanField('Горячие предложения ?', default=False)
    is_in_ya_feed = models.BooleanField('Выгружать в Яндекс фид ?', default=False)
    action_type = models.CharField('Тип', max_length=2, choices=ACTION_TYPE_CHOICES, default=TO_RENT)
    street = models.CharField('Улица', max_length=255, blank=False, null=True)
    street_number = models.CharField('Номер дома', max_length=255, blank=False, null=True)
    room_number = models.CharField('Номер квартиры', max_length=255, blank=True, null=True)
    cadaster_number = models.CharField('Кадастровый номер', max_length=255, blank=True, null=True)
    town = models.ForeignKey(Town, on_delete=models.CASCADE, blank=False, null=True, verbose_name='Город')
    floor = models.IntegerField('Этаж', blank=True, null=True)
    floor_total = models.IntegerField('Этажность', blank=True, null=True)
    house_type = models.CharField('Тип', max_length=2, choices=HOUSE_TYPE_CHOICES, blank=True, null=True)
    rooms = models.CharField('Комнат', max_length=2, choices=ROOMS_NUMBER_CHOICES, blank=True, null=True)
    balkon_type = models.CharField('Балкон', max_length=2, choices=BALKON_TYPE_CHOICES,blank=True, null=True)
    square_total = models.IntegerField('Площадь общая', blank=True, null=True)
    square_living = models.IntegerField('Площадь жилая', blank=True, null=True)
    square_kitchen = models.IntegerField('Площадь кухни', blank=True, null=True)
    square_room = models.IntegerField('Площадь комнаты', blank=True, null=True)
    square_land = models.IntegerField('Площадь земли', blank=True, null=True)
    land_type = models.CharField('Категория земель', max_length=2, choices=LAND_TYPE_CHOICES, blank=True, null=True)
    order_type = models.CharField('Тип сделки', max_length=2, choices=ORDER_TYPE_CHOICES, blank=True, null=True)
    own_years = models.CharField('Лет в собственности', max_length=2, choices=OWN_YEARS_CHOICES, blank=True, null=True)
    contact_name = models.CharField('Контактное лицо (собственник)', blank=False, max_length=255, null=True)
    contact_phone = models.CharField('Телефон (собственник)', blank=False, max_length=255, null=True)
    contact_email = models.CharField('Email (собственник)', blank=True, max_length=255, null=True)
    description = models.TextField('Описание', blank=True, null=True)
    currency_type = models.CharField('Тип', max_length=2, choices=CURRENCY_CHOICES, default=RUB)
    price = models.IntegerField('Цена', blank=False, null=True)
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)
    updated_at = models.DateTimeField('Изменено', auto_now=True)

    # def get_absolute_url(self):
    #     return f'/article/{self.name_slug}/'
    # def save(self, *args, **kwargs):
    #     self.number = f'01-{10000 + self.id}'
    #     super(Ads, self).save(*args, **kwargs)

    def __str__(self):
        return f'Номер объекта: {self.number} | Категория : {self.category.name} '

    class Meta:
        verbose_name = "Обьявление"
        verbose_name_plural = "Обьявления"

def ads_post_save(sender, instance, created, **kwargs):
   if created:
       instance.number = f'01-{10000 + instance.id}'
       instance.save()

post_save.connect(ads_post_save, sender=Ads)


class AdsImage(models.Model):
    ads = models.ForeignKey(
        Ads,
        blank=False,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Для обьявления",
    )
    image = models.ImageField('Изображение', blank=False, null=True,upload_to='ads/image')
    image_thumb = models.ImageField('Изображение', blank=True, null=True,upload_to='ads/image', editable=False)
    image_main = models.ImageField('Изображение', blank=True, null=True,upload_to='ads/image', editable=False)

    def save(self, *args, **kwargs):

        #уменьшение превью изображения до 200х200
        if self.image:
            fill_color = '#fff'
            base_image = Image.open(self.image)
            if base_image.mode in ('RGBA', 'LA'):
                background = Image.new(base_image.mode[:-1], base_image.size, fill_color)
                background.paste(base_image, base_image.split()[-1])
                base_image = background
            blob_thumb = BytesIO()
            blob_main = BytesIO()
            width, height = base_image.size
            transparent_thumb = Image.new('RGB', (width, height), (0, 0, 0, 0))
            transparent_thumb.paste(base_image, (0, 0))
            transparent_thumb.thumbnail((80, 50), Image.ANTIALIAS)
            transparent_thumb.save(blob_thumb, 'JPEG')

            transparent_main = Image.new('RGB', (width, height), (0, 0, 0, 0))
            transparent_main.paste(base_image, (0, 0))
            transparent_main.thumbnail((445, 280), Image.ANTIALIAS)
            transparent_main.save(blob_main, 'JPEG')

            self.image_thumb.save(f'{self.ads.id}-{self.ads.number}-thumb.jpg', File(blob_thumb), save=False)
            self.image_main.save(f'{self.ads.id}-{self.ads.number}-main.jpg', File(blob_main), save=False)
        super(AdsImage, self).save(*args, **kwargs)

    def __str__(self):
        return f"Фото для объявления №{self.ads.number} "

    class Meta:
        verbose_name = "Фото для объявления"
        verbose_name_plural = "Фото для объявлений"