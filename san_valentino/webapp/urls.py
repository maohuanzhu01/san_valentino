from django.urls import path
from . import views

urlpatterns = [
    path('calculate-days/', views.calculate_days, name='calculate_days'),
]