# Generated by Django 4.0.4 on 2022-06-29 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='сalculation_of_flange_bolts',
            name='count_bolts',
            field=models.IntegerField(help_text='Введите количество болтов', verbose_name='Количество болтов'),
        ),
        migrations.AlterField(
            model_name='сalculation_of_flange_bolts',
            name='diametr_bolta',
            field=models.IntegerField(help_text='Введите диаметр болта', verbose_name='Диаметр болта'),
        ),
    ]
