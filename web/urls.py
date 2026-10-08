from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('plantilla1/', views.plantilla1, name='plantilla1'),
    path('plantilla2/', views.plantilla2, name='plantilla2'),
    path('plantilla3/', views.plantilla3, name='plantilla3'),
    path('plantilla4/', views.plantilla4, name='plantilla4'),
]