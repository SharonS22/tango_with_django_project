# Generated by Django 2.1.5 on 2022-02-09 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_auto_20220209_1405'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name_plural': 'Pages'},
        ),
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]
