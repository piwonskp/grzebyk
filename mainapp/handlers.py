from django.db.models.signals import pre_init
from django.dispatch import receiver

from mainapp.models import ArticleImage, ProductImage, Image


@receiver(pre_init, sender=ProductImage)
def pre_init_product_image(sender, *args, **kwargs):
    kwargs['upload_to'] = 'shop'

@receiver(pre_init, sender=ProductImage)
def pre_init_article_image(sender, **kwargs):
    print('artim')
    kwargs['upload_to'] = 'articles'

@receiver(pre_init, sender=Image)
def pre_init_image(sender, *args, **kwargs):
    print('im')
    sender.upload_to = kwargs.pop('upload_to', '')
    Image.upload_to = sender.upload_to
    print('klasa:', Image.upload_to)
    print('inst:', self.upload_to)
    print('image:', self.image.upload_to)
