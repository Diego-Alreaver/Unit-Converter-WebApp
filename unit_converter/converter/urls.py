# converter/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('length/', views.length_conversion, name='length_conversion'),
    path('weight/', views.weight_conversion, name='weight_conversion'),
    path('temperature/', views.temperature_conversion, name='temperature_conversion'),
]
