from django.urls import path
from . import views

urlpatterns = [
    path('appointments/', views.appointments, name='appointments'),
    path('appointment/<int:id>/', views.appointment, name='appointment'),
]
