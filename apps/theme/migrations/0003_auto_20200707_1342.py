# Generated by Django 3.0.8 on 2020-07-07 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0002_homepage_head_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='head_image',
            field=models.ImageField(default='/media/head_img/log.svg', upload_to='head_image', verbose_name='用户头像'),
        ),
    ]
