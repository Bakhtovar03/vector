from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import DetailView
from .models import UserProfile


class UserLoginView(SuccessMessageMixin,LoginView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm
    next_page = '/'
    success_message = 'Вход успешно выполнен!'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Вход в аккаунт'
        return context

class UserLogoutView(SuccessMessageMixin,LogoutView):
    next_page = '/'
    success_message = 'Вы вышли из аккаунта'
    success_url = '/'

class UserProfileView(DetailView):
    model = UserProfile
    template_name = 'accounts/profile.html'
    context_object_name = 'profile'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Профиль пользователя'
        return context
