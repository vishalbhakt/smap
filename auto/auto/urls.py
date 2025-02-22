"""
URL configuration for auto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('teamreg/',views.teamreg,name='teamreg'),
    path('treg/',views.treg,name='treg'),
    path('normalreg/',views.normalreg,name='normalreg'),
    path('nreg/',views.nreg,name='nreg'),
    path('validate/',views.validate,name='validate'),
    path('tmhome/',views.tmhome,name='tmhome'),
    path('normalhome/',views.normalhome,name='normalhome'),

]
