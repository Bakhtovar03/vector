from django.urls import path
from .views import *


urlpatterns = [
    path('logout/', UserLogoutView.as_view(),name='logout'),
    path('login/', UserLoginView.as_view(),name='login'),
    path('profile/<slug:slug>/', UserProfileView.as_view(),name='profile'),
]