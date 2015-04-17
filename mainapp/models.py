from django.db import models

from imagekit import ImageSpec, register
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from imagekit.utils import get_field_info


class Article(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField('Data publikacji')
    content = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
        verbose_name = "artykuł"
        verbose_name_plural = "artykuły"


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'produkt'
        verbose_name_plural = 'produkty'


class ImageThumbnail(ImageSpec):
    @property
    def processors(self):
        model, field_name = get_field_info(self.source)
        return [ResizeToFill(model.THUMB_WIDTH, model.THUMB_HEIGHT)]

register.generator('mainapp:image:image_thumbnail', ImageThumbnail)


def upload_to(instance, filename):
    switch = {ArticleImage: 'articles', ProductImage: 'shop'}
    directory = switch.pop(instance.__class__, '')
    return '/'.join([directory, filename])


class Image(models.Model):
    THUMB_WIDTH = 100
    THUMB_HEIGHT = 70
    image = models.ImageField(upload_to=upload_to, null=True)
    image_thumbnail = ImageSpecField(source='image',
                                     id='mainapp:image:image_thumbnail',
                                     format='JPEG',
                                     options={'quality': 60})

    class Meta:
        abstract = True


class ArticleImage(Image):
    article = models.ForeignKey(Article, related_name='images')


class ProductImage(Image):
    product = models.OneToOneField(Product)
    THUMB_WIDTH = 168
    THUMB_HEIGHT = 117
