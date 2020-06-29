from django.db import models

class Vacancy(models.Model):
    title = models.CharField('Название вакансии', max_length=255,blank=False,null=True)
    option1 = models.CharField('Опция вакансии', max_length=255,blank=True,null=True,
                               default='Бесплатное обучение')
    option2 = models.CharField('Опция вакансии', max_length=255, blank=True, null=True,
                               default='Быстрый старт в профессии под руководством опытного наставника')
    option3 = models.CharField('Опция вакансии', max_length=255, blank=True, null=True,
                               default='Перспективы профессионального развития и карьерного роста')
    option4 = models.CharField('Опция вакансии', max_length=255, blank=True, null=True)
    is_active = models.BooleanField('Активна ?', default=True)

    def __str__(self):
        if self.is_active:
            return f"Активная вакансия {self.title} "
        else:
            return f"Не активная вакансия {self.title} "

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

class VacancyApply(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Вакаксия')
    name = models.CharField('Имя', max_length=255, blank=False, null=True)
    email = models.CharField('Email', max_length=255, blank=False, null=True)
    resume = models.FileField('Резюме', blank=True,null=True)
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)

    def __str__(self):
        return f"Отзыв на вакансию {self.vacancy.title} "

    class Meta:
        verbose_name = "Отзыв на вакансию"
        verbose_name_plural = "Отзывы на вакансии"


class Consultation(models.Model):
    category = models.CharField('Город', blank=True, max_length=255, null=True)
    town = models.CharField('Город', blank=True, max_length=255, null=True)
    name = models.CharField('Контактное лицо ', blank=True, max_length=255, null=True)
    phone = models.CharField('Телефон ', blank=True, max_length=255, null=True)
    email = models.CharField('Email ', blank=True, max_length=255, null=True)
    description = models.TextField('Описание', blank=True, null=True)
    currency_type = models.CharField('Валюта', max_length=15, )
    price = models.IntegerField('Цена', blank=True, null=True)
    street = models.CharField('Улица', max_length=255, blank=True, null=True)
    street_number = models.CharField('Номер дома', max_length=255, blank=True, null=True)
    floor = models.IntegerField('Этаж', blank=True, null=True)
    floor_total = models.IntegerField('Этажность', blank=True, null=True)
    rooms = models.CharField('Комнат', max_length=10, blank=True, null=True)
    square_total = models.IntegerField('Площадь общая', blank=True, null=True)
    square_kitchen = models.IntegerField('Площадь кухни', blank=True, null=True)
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)
    is_viewed = models.BooleanField('Обработана ?', default=False)

    def __str__(self):
        return f"Заявка на консультацию  "

    class Meta:
        verbose_name = "Заявка на консультацию"
        verbose_name_plural = "Заявки на консультацию"