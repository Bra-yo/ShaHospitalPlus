from django.contrib import admin
from django.urls import path
from HospitalApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('starter/', views.starter, name='starter'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('departments/', views.departments, name='departments'),
    path('doctors/', views.doctors, name='doctors'),
    path('contact/', views.contact, name='contact'),
    path('appointment/', views.appoint, name='appointment'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>', views.delete),
path('all contacts/', views.cnts, name='cnts'),

    path('delcont/<int:id>', views.delcont),
]
