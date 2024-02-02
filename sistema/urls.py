from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página de inicio
    path('base/', views.base, name='base'),  # Página base (si es necesario)
]
