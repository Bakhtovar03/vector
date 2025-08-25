from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from content.models import Course, Teacher


class HomePageView(TemplateView):
    template_name = 'content/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'

class CourseListView(ListView):
    template_name = 'content/course_list.html'
    model = Course
    context_object_name = 'courses'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']= 'Курсы'
        return context
class CourseDetailView(DetailView):
    template_name = 'content/course_detail.html'
    model = Course
    context_object_name = 'course'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        return context

class TeacherListView(ListView):
    template_name = 'content/teacher_list.html'
    model = Teacher
    context_object_name = 'teachers'
    paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Наши преподаватели'
        return context