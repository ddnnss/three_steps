from django.db import models
from django.utils.safestring import mark_safe
from customuser.models import User
from django.db.models.signals import post_save
from django.core.files import File
from io import BytesIO
from pytils.translit import slugify
from PIL import Image



class Category(models.Model):
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    name_slug = models.CharField(blank=True, max_length=255, null=True, editable=False)


    def save(self, *args, **kwargs):
        #создание имени для ЧПУ ссылки
        self.name_slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} '

    class Meta:
        verbose_name = "Тип нежвижимости"
        verbose_name_plural = "Типы нежвижимости"

class SubCategory(models.Model):
    category = models.ForeignKey(Category, blank=False,null=True,on_delete=models.CASCADE,verbose_name='Относится к')
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    name_slug = models.CharField(blank=True, max_length=255, null=True, editable=False)
    show_square_kitchen = models.BooleanField('Показывать площадь кухни в форме на главной?', default=True)
    show_building_type = models.BooleanField('Показывать новострой/вторичка главной?', default=True)
    show_square_land = models.BooleanField('Показывать площадь земли в форме на главной?', default=False)
    show_total_square = models.BooleanField('Показывать общую площадь  в форме на главной?', default=True)
    show_floors = models.BooleanField('Показывать этажи/этажность в форме на главной?', default=True)
    show_rooms = models.BooleanField('Показывать кол-во комнат в форме на главной?', default=True)
    show_house_type = models.BooleanField('Показывать тип постройки в форме на главной?', default=True)

    def save(self, *args, **kwargs):
        #создание имени для ЧПУ ссылки
        self.name_slug = slugify(self.name)
        super(SubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} '

    class Meta:
        verbose_name = "Под тип нежвижимости"
        verbose_name_plural = "Под типы нежвижимости"

class Metro(models.Model):
    name = models.CharField('Метро', max_length=255, blank=False, null=True)
    name_slug = models.CharField(blank=True, max_length=255, null=True, editable=False)

    def save(self, *args, **kwargs):
        #создание имени для ЧПУ ссылки
        self.name_slug = slugify(self.name)
        super(Metro, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} '

    class Meta:
        verbose_name = "Метро"
        verbose_name_plural = "Метро"

class Town(models.Model):
    metros = models.ManyToManyField(Metro,blank=True,null=True,verbose_name='Возможные метро')
    name = models.CharField('Город', max_length=255, blank=False, null=True)
    name_slug = models.CharField(blank=True, max_length=255, null=True, editable=False)

    def save(self, *args, **kwargs):
        # создание имени для ЧПУ ссылки
        self.name_slug = slugify(self.name)
        super(Town, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} '

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

    f1 = 'F1'
    f2 = 'F2'
    f3 = 'F3'
    f4 = 'F4'
    f5 = 'F5'
    f6 = 'F6'
    f7 = 'F7'
    f8 = 'F8'
    f9 = 'F9'
    f10 = 'F10'
    f11 = 'F11'

    FEED_CATEGORY_CHOICES = [
        (f1, 'дача'),
        (f2, 'коттедж'),
        (f3, 'дом'),
        (f4, 'дом с участком'),
        (f5, 'участок'),
        (f6, 'часть дома'),
        (f7, 'квартира'),
        (f8, 'комната'),
        (f9, 'таунхаус'),
        (f10, 'дуплекс'),
        (f11, 'гараж'),

    ]

    s1 = 'S1'
    s2 = 'S2'
    s3 = 'S3'
    s4 = 'S4'
    s5 = 'S5'
    s6 = 'S6'


    FEED_STATUS_CHOICES = [
        (s1, 'первичная продажа'),
        (s2, 'продажа от застройщика'),
        (s3, 'переуступка'),
        (s4, 'прямая продажа'),
        (s5, 'первичная продажа вторички'),
        (s6, 'встречная продажа'),




    ]



    created = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Добавил')
    number = models.CharField('Номер объекта', max_length=255, blank=True, null=True, editable=False)
    name = models.CharField('Заголовок', blank=False, max_length=255, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True,verbose_name='Тип недвижимости', editable=False)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=False, null=True,verbose_name='Под тип недвижимости')
    metro = models.ForeignKey(Metro, on_delete=models.CASCADE, blank=True, null=True,verbose_name='Метро')
    is_new_building = models.BooleanField('Новострой ?', default=False)

    is_checked = models.BooleanField('Проверено ?', default=False)
    is_publish = models.BooleanField('Опубликован ?', default=False)
    is_hot = models.BooleanField('Горячие предложения ?', default=False)
    built_year = models.CharField('Год сдачи (Для фида)', max_length=255, blank=False, null=True)
    feed_category = models.CharField('Категория объекта (Для фида)', max_length=20, choices=FEED_CATEGORY_CHOICES, default=f1)
    feed_deal_status = models.CharField('Тип сделки (Для фида)', max_length=20, choices=FEED_STATUS_CHOICES, default=s1)
    is_living = models.BooleanField('Жилая? (Для фида)', default=True)
    is_in_ya_feed = models.BooleanField('Выгружать в Яндекс фид ?', default=False)
    action_type = models.CharField('Тип сделки', max_length=20, choices=ACTION_TYPE_CHOICES, default=TO_RENT)
    street = models.CharField('Улица', max_length=255, blank=False, null=True)
    street_number = models.CharField('Номер дома', max_length=255, blank=False, null=True)
    room_number = models.CharField('Номер квартиры', max_length=255, blank=True, null=True)
    cadaster_number = models.CharField('Кадастровый номер', max_length=255, blank=True, null=True)
    town = models.ForeignKey(Town, on_delete=models.CASCADE, blank=False, null=True, verbose_name='Город')
    floor = models.IntegerField('Этаж', blank=True, null=True)
    floor_total = models.IntegerField('Этажность', blank=True, null=True)
    house_type = models.CharField('Тип постройки', max_length=20, choices=HOUSE_TYPE_CHOICES, blank=True, null=True)
    rooms = models.CharField('Комнат', max_length=20, choices=ROOMS_NUMBER_CHOICES, blank=True, null=True)
    balkon_type = models.CharField('Балкон', max_length=20, choices=BALKON_TYPE_CHOICES,blank=True, null=True)
    square_total = models.IntegerField('Площадь общая', blank=True, null=True)
    square_living = models.IntegerField('Площадь жилая', blank=True, null=True)
    square_kitchen = models.IntegerField('Площадь кухни', blank=True, null=True)
    square_room = models.IntegerField('Площадь комнаты', blank=True, null=True)
    square_land = models.IntegerField('Площадь земли', blank=True, null=True)
    land_type = models.CharField('Категория земель', max_length=20, choices=LAND_TYPE_CHOICES, blank=True, null=True)
    order_type = models.CharField('Тип сделки', max_length=20, choices=ORDER_TYPE_CHOICES, blank=True, null=True)
    own_years = models.CharField('Лет в собственности', max_length=20, choices=OWN_YEARS_CHOICES, blank=True, null=True)
    contact_name = models.CharField('Контактное лицо (собственник)', blank=False, max_length=255, null=True)
    contact_phone = models.CharField('Телефон (собственник)', blank=False, max_length=255, null=True)
    contact_email = models.CharField('Email (собственник)', blank=True, max_length=255, null=True)
    description = models.TextField('Описание', blank=True, null=True)
    currency_type = models.CharField('Валюта', max_length=20, choices=CURRENCY_CHOICES, default=RUB)
    price = models.IntegerField('Цена', blank=False, null=True)
    ads_type = models.CharField('Объявления с сайта',max_length=50, blank=True, null=True)
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)
    updated_at = models.DateTimeField('Изменено', auto_now=True)

    def get_absolute_url(self):
        return f'/ads/{self.number}/'
    # def save(self, *args, **kwargs):
    #     self.number = f'01-{10000 + self.id}'
    #     super(Ads, self).save(*args, **kwargs)
    def get_images(self):
        return self.images.all()

    def get_currency(self):
         if self.currency_type == 'RU':
             return '₽'
         else:
            return '$'
    def get_feed_rooms(self):
        if self.rooms == 'R1':
            return '1'
        if self.rooms == 'R2':
            return '2'
        if self.rooms == 'R3':
            return '3'
        if self.rooms == 'R4':
            return '4'
        if self.rooms == 'R5':
            return '5'

    def get_feed_status(self):
        if self.feed_deal_status == 'S1':
            return 'первичная продажа'
        if self.feed_deal_status == 'S2':
            return 'продажа от застройщика'
        if self.feed_deal_status == 'S3':
            return 'переуступка'
        if self.feed_deal_status == 'S4':
            return 'прямая продажа'
        if self.feed_deal_status == 'S5':
            return 'первичная продажа вторички'
        if self.feed_deal_status == 'S5':
            return 'встречная продажа'

    def get_action_type(self):
        if self.action_type == self.TO_RENT:
            return 'Сдается'
        elif self.action_type == self.SELL:
            return 'Продается'
    def get_feed_cat(self):
        if self.feed_category == 'F1':
            return 'дача'
        if self.feed_category == 'F2':
            return 'коттедж'
        if self.feed_category == 'F3':
            return 'дом'
        if self.feed_category == 'F4':
            return 'дом с участком'
        if self.feed_category == 'F5':
            return 'участок'
        if self.feed_category == 'F6':
            return 'часть дома'
        if self.feed_category == 'F7':
            return 'квартира'
        if self.feed_category == 'F8':
            return 'комната'
        if self.feed_category == 'F9':
            return 'таунхаус'
        if self.feed_category == 'F10':
            return 'дуплекс'
        if self.feed_category == 'F11':
            return 'гараж'

    def get_ads_type(self):
        if self.square_land:
            return f'земельный участок {self.square_land}'
        else:
            return f'{self.get_rooms_display()}к. {self.subcategory.name.lower()}'

    def get_square(self):
        if self.square_land:
            return f'{self.square_land  if self.square_land else "" }'
        else:
            return f'{str(self.square_total) + "/" if  self.square_total else "" }' \
                   f'{str(self.square_living) + "/" if self.square_living else "" }' \
                   f'{self.square_kitchen  if self.square_kitchen else "" }'

    def get_floors(self):
        return f'{str(self.floor) + "/"  if self.floor else "" }' \
               f'{self.floor_total  if self.floor_total else "" }, '

    def split_descrition(self):

        description = ''
        for line in self.description.split('\n'):
            description += f'<p>{line}</p>'
        return description

    def get_own_years_val(self):
        if self.own_years:
            return f'{self.get_own_years_display()} в собственности,'
        else:
            return ''
    def get_order_type_val(self):
        if self.order_type:
            return f'{self.get_order_type_display()} ,'
    def get_phone(self):
        return f'{self.contact_phone.replace("+","").replace("(","").replace(")","").replace("-","").replace(" ","")}'

    def get_full_description(self):
        return f'<p>{self.get_action_type()} {self.get_ads_type()}, {self.town.name} {self.street} {self.street_number}, ' \
               f'{self.get_square()}, {self.get_floors()} {self.get_house_type_display()}</p>' \
               f'{self.split_descrition()}' \
               f'<p>{self.get_own_years_val()} {self.get_order_type_val()} {self.price} {self.get_currency()}, ' \
               f'{self.contact_name}, <a href="tel:{self.get_phone()}">{self.contact_phone}</a></p>'

    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        if self.images.exists():
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.images.first().image_thumb.url))
        else:
            return mark_safe('<span>Нет загружениых фото</span>')

    image_tag.short_description = 'Фото'

    def __str__(self):
        return f'Номер объекта: {self.number} | Категория : {self.category.name} '

    class Meta:
        verbose_name = "Обьявление"
        verbose_name_plural = "Обьявления"

def ads_post_save(sender, instance, created, **kwargs):
   if created:
       instance.category = instance.subcategory.category
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
        related_name='images'
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

    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        if self.image_thumb:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image_thumb.url))
        else:
            return mark_safe('<span>Нет загружениых фото</span>')

    def __str__(self):
        return f"Фото для объявления №{self.ads.number} "

    class Meta:
        verbose_name = "Фото для объявления"
        verbose_name_plural = "Фото для объявлений"