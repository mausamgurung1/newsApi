from django.contrib import admin
from django.urls import path

from newsapp import views

app_name = 'newsapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls, name='admin'),
]
