# Generated by Django 4.1.3 on 2022-12-27 10:57

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='main_picture',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=-1, scale=None, size=[600, 400], upload_to='%m'),
        ),
    ]