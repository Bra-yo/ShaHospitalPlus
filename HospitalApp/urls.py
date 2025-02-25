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

]
