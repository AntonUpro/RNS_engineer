from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Сalculation_of_flange_bolts(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Пользователь", help_text="Пользователь выполнивший расчет")
    name=models.CharField(max_length=30, help_text='Введите название вашего расчета', verbose_name='Название расчета')
    foundation_bolts=models.BooleanField(help_text='Фундаментные болты', verbose_name='Фундаментные болты', null=True, blank=True)
    on_bolt=models.BooleanField(help_text='Установлены ли на шпильках', verbose_name='Установка на шпильки', null=True, blank=True)
    count_bolts=models.IntegerField(help_text='Введите количество болтов', verbose_name='Количество болтов в мм')
    bolt_strength_class=models.CharField(max_length=4, help_text='Выберите класс прочности болтов', verbose_name='Класс прочности болтов')
    diametr_bolta=models.IntegerField(help_text='Введите диаметр болта', verbose_name='Диаметр болта')
    circle_diameter=models.IntegerField(help_text='Введите диаметр окружности, по которому расположены болты', verbose_name='Диаметр окружности в мм')
    stress_N=models.IntegerField(help_text='Введите продольную силу N в тс', verbose_name='Продольная сила N в кг')
    stress_M=models.FloatField(help_text='Введите момент M в тс*м', verbose_name='Момент M в тс*м')
    index_dinamic=models.FloatField(help_text='Выберите коэфициент динамичности', verbose_name='Коэфициент динамичности', default=1)
    result_calc=models.CharField(help_text='Введите название вашего расчета', verbose_name='Результ расчета', max_length=30, default=0)
    result_calc_doc=models.FileField(help_text='Путь к файлу', null=True, blank=True)


# Create your models here.
