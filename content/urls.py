from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('courses/teachers/', views.TeacherListView.as_view(), name='teacher_list'),
    path('courses/subscribe/<int:course_id>/', views.SubscribeView.as_view(), name='subscribe'),
    path('courses/<slug:slug>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('courses/', views.CourseListView.as_view(), name='course_list'),
    path('', HomePageView.as_view(), name='home'),

]