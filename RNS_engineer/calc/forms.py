from django import forms


bolt_strength_class_choise=(('5.6','5.6'),('5.8','5.8'),('8.8','8.8'),('10.9','10.9'),('12.9','12.9'))
index_dinamic1=((1,1),(1.05,1.05),(1.18,1.18),(1.35,1.35))

class Сalculation_of_flange_bolts_Form(forms.Form):
    name=forms.CharField(label='Название расчета')
    foundation_bolts=forms.BooleanField(label='Фундаментные болты', required=False)
    on_bolt=forms.BooleanField(help_text='Установка на шпильки', required=False)
    count_bolts=forms.IntegerField(label='Введите количество болтов')
    bolt_strength_class=forms.ChoiceField(choices=bolt_strength_class_choise, label='Класс просности', help_text='Выберите класс прочности болтов')
    diametr_bolta=forms.IntegerField(label='Диаметр болта', help_text='Введите диаметр болта в мм')
    circle_diameter=forms.FloatField(label='Диаметр окружности, по которому расположены болты')
    stress_N=forms.FloatField(help_text='Введите продольную силу N в тс', label='Продольная сила N в кг')
    stress_M=forms.FloatField(help_text='Введите момент M в тс*м', label='Момент M в тс*м')
    index_dinamic=forms.ChoiceField(choices=index_dinamic1 ,help_text='Выберите коэфициент динамичности', label='Коэфициент динамичности')
    # result_calc=forms.CharField(help_text='Результат расчета', label='Результ расчета')
