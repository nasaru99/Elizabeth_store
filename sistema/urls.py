from django.urls import path
from . import views
from .views import CustomLoginView, logout_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='index'), 
    path('base/', views.base, name='base'), 
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
]
