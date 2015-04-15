# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

products = []
articles = []

def reg_globals(apps, schema_editor):
    ArticleImage = apps.get_model("mainapp", "ArticleImage")
    ProductImage = apps.get_model("mainapp", "ProductImage")
    global products
    global articles
    for product in ProductImage.objects.all():
        products.append(product)
    for article in ArticleImage.objects.all():
        articles.append(article)

def migrate_data(apps, schema_editor):
    ArticleImage = apps.get_model("mainapp", "ArticleImage")
    ProductImage = apps.get_model("mainapp", "ProductImage")
    global products
    global articles
    i=0
    for product in ProductImage.objects.all():
        print(products[i].image_ptr.image.url)
        product.image = products[i].image_ptr.image
        product.save()
        i+=1
    i=0
    for article in ArticleImage.objects.all():
        print(articles[i].image_ptr.image.url)
        article.image = articles[i].image_ptr.image
        article.save()
        i+=1


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20150412_2056'),
    ]

    operations = [
        migrations.RunPython(reg_globals),

        migrations.AlterField(
            model_name='productimage',
            name='image_ptr',
            field=models.IntegerField(serialize=False, primary_key=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articleimage',
            name='image_ptr',
            field=models.IntegerField(serialize=False, primary_key=False),
            preserve_default=False,
        ),

        migrations.AddField(
            model_name='articleimage',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articleimage',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productimage',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productimage',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to=''),
            preserve_default=False,
        ),

        migrations.RunPython(migrate_data),

        migrations.RemoveField(
            model_name='articleimage',
            name='image_ptr',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='image_ptr',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
