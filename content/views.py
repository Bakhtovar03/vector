from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.conf import settings
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.core.mail import send_mail
from content.forms import SubscribeForm
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


class SubscribeView(SuccessMessageMixin, FormView):
    template_name = 'content/subscribe.html'
    form_class = SubscribeForm
    model = Course
    context_object_name = 'course'
    success_message = 'Ваша заявка успешно отправлена, скоро с вами свяжемся!'

    def get_success_url(self):
        course_id = self.kwargs['course_id']
        course = Course.objects.get(id=course_id)
        return course.get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course_id = self.kwargs['course_id']
        context['title'] = f'Запись на курс "{Course.objects.get(id=course_id).name}"'
        return context

    def form_valid(self, form):
        course_id = self.kwargs['course_id']
        course = Course.objects.get(id=course_id)
        subject = f'Новая запись на курс "{course.name}"'

        message = f'ФИО: {form.cleaned_data["name"]}\n\
        ФИО ребёнка: {form.cleaned_data["children_name"]}\n\
        Возраст ребенка: {form.cleaned_data["children_age"]}\n\
        Способы связи: {form.cleaned_data["contact_method"]}\n\
        Номер для связи: {form.cleaned_data["contact"]}\n\
        Ссылка на VK: {form.cleaned_data["vk_url"] or "отсутствует"}'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        return super().form_valid(form)





