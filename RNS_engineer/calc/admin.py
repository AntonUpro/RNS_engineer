from django.contrib import admin
from .models import Сalculation_of_flange_bolts

class Сalculation_of_flange_bolts_admin(admin.ModelAdmin):
    list_display=('user_id','name','count_bolts','diametr_bolta','circle_diameter')
 
admin.site.register(Сalculation_of_flange_bolts, Сalculation_of_flange_bolts_admin)


# Register your models here.
