from ckeditor_uploader.fields import RichTextUploadingField


from django.db import models
from django.core.files import File
from io import BytesIO
from pytils.translit import slugify
from PIL import Image




class Article(models.Model):

    name = models.CharField('Название статьи', max_length=120, blank=False, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, editable=False, db_index=True)
    image = models.ImageField('Изображение превью 200x200)', upload_to='article/', blank=False,null=True)
    page_title = models.CharField('Тэг Title', max_length=255, blank=True, null=True)
    page_description = models.TextField('Тэг Description', blank=True, null=True)

    text = RichTextUploadingField('Статья.', blank=False, null=True)
    views = models.IntegerField('Просмотров', default=0)
    is_active = models.BooleanField('Отображать статью ?', default=True, db_index=True)
    created_at = models.DateTimeField('Создана',auto_now_add=True)

    def get_preview_image(self):
        if self.image:
            return self.image.url
        else:
            return ''

    def save(self, *args, **kwargs):
        #создание имени для ЧПУ ссылки
        self.name_slug = slugify(self.name)

        #уменьшение превью изображения до 200х200
        # if self.image:
        #     fill_color = '#fff'
        #     base_image = Image.open(self.image)
        #     if base_image.mode in ('RGBA', 'LA'):
        #         background = Image.new(base_image.mode[:-1], base_image.size, fill_color)
        #         background.paste(base_image, base_image.split()[-1])
        #         base_image = background
        #     blob = BytesIO()
        #     width, height = base_image.size
        #     transparent = Image.new('RGB', (width, height), (0, 0, 0, 0))
        #     transparent.paste(base_image, (0, 0))
        #     transparent.thumbnail((200, 200), Image.ANTIALIAS)
        #     transparent.save(blob, 'JPEG')
        #     self.image.save(f'{self.name_slug}.jpg', File(blob), save=False)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/articles/{self.name_slug}/'

    def __str__(self):
        return f'id: {self.id} | Статья : {self.name}'

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"




