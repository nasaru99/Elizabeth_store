from django.shortcuts import render, redirect
from .models import Producto  
# from .forms import CustomAuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout


def index(request):
    productos = Producto.objects.all()  
    return render(request, 'index.html', {'productos': productos})

def base(request):
    return render(request, 'base.html')

# class CustomLoginView(LoginView):
#     authentication_form = CustomAuthenticationForm
#     template_name = 'login/login.html'
#     success_url = reverse_lazy('index')
#     def get_success_url(self):
#         return self.success_url
    

def logout_view(request):
     logout(request)
     return redirect('index')

class CustomLoginView(LoginView):
    template_name = 'login/login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('index')