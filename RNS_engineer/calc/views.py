from django.http import HttpResponse
from django.shortcuts import render
from .models import Сalculation_of_flange_bolts
from .Calc_of_flange_bolts import calc_F
from .forms import Сalculation_of_flange_bolts_Form


def index(request):
    return render(request, 'index.html',{'tit':'Ghjdthrf'})

def Сalculation_of_flange_bolts_add(request):
    calc=Сalculation_of_flange_bolts()
    form=Сalculation_of_flange_bolts_Form()
    if request.method=='POST':
        calc.name=request.POST.get('name')
        calc.foundation_bolts=request.POST.get('foundation_bolts')
        calc.on_bolt=request.POST.get('on_bolt')
        calc.count_bolts=request.POST.get('count_bolts')
        calc.bolt_strength_class=request.POST.get('bolt_strength_class')
        calc.diametr_bolta=request.POST.get('diametr_bolta')
        calc.circle_diameter=request.POST.get('circle_diameter')
        calc.stress_N=request.POST.get('stress_N')
        calc.stress_M=request.POST.get('stress_M')
        calc.index_dinamic=request.POST.get('index_dinamic')
        calc.save()
        calc.result_calc=calc_F(calc.foundation_bolts,calc.on_bolt,calc.count_bolts,calc.bolt_strength_class,
        calc.diametr_bolta,calc.circle_diameter,calc.stress_N,calc.stress_M,calc.index_dinamic)
        calc.save()
    list_calc={'form':form,'result_calc':calc.result_calc}
    return render(request, "calc/flange_bolts.html", list_calc)

    


# Create your views here.
