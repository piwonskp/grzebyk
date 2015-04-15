from django.db import models
from django.db.models.signals import pre_init

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


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


class Image(models.Model):
        upload_to = ''
        thumb_width = 100
        thumb_height = 70
        image = models.ImageField(upload_to=upload_to, null=True)
        image_thumbnail = ImageSpecField(source='image',
                                         processors=[ResizeToFill(thumb_width, thumb_height)],
                                         format='JPEG',
                                         options={'quality': 60})

        class Meta:
            abstract = True


class ArticleImage(Image):
    article = models.ForeignKey(Article, related_name='images')

    def __init__(self, *args, **kwargs):
        self._meta.get_field('image').upload_to = 'articles'
        super(ArticleImage, self).__init__(*args, **kwargs)


class ProductImage(Image):
    product = models.OneToOneField(Product)

    def __init__(self, *args, **kwargs):
        self._meta.get_field('image').upload_to = 'shop'
        super(ProductImage, self).__init__(*args, **kwargs)
