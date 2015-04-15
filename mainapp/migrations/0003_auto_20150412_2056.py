# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_articleimage_productimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='articleimage',
            name='id',
        ),
        migrations.RemoveField(
            model_name='articleimage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='id',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='image',
        ),
        migrations.AddField(
            model_name='articleimage',
            name='image_ptr',
            field=models.OneToOneField(primary_key=True, serialize=False, to='mainapp.Image', auto_created=True, default=None, parent_link=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productimage',
            name='image_ptr',
            field=models.OneToOneField(primary_key=True, serialize=False, to='mainapp.Image', auto_created=True, default=None, parent_link=True),
            preserve_default=False,
        ),
    ]
