"""RNS_engineer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path, include
from calc import views as cviews
from Users import views
from django.contrib.auth import urls


urlpatterns = [
    path('', cviews.index, name='index'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('flange_bolts/', cviews.Сalculation_of_flange_bolts_add, name='flange_bolts'),
    path('admin/', admin.site.urls),
]

urlpatterns+=urls.urlpatterns