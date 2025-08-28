from datetime import datetime

from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from pytils.translit import slugify

class Teacher(models.Model):
    """"Модель Преподавателя"""

    name = models.CharField(max_length=100,verbose_name='Имя')

    last_name = models.CharField(max_length=100,verbose_name='фамилия')

    subjects_taught = models.CharField(max_length=250,verbose_name='преподаваемые предметы')

    info = models.TextField(verbose_name='Дополнительная информация')

    avatar = models.ImageField(default='avatars/default.png',
                               upload_to='avatars/%Y/%m',null = True,blank = True,
                               validators=[FileExtensionValidator(['jpg','png','jpeg','webp'])])

    updated_at = models.DateTimeField(auto_now=True)

    birthday = models.DateField(verbose_name='Дата рождения')

    class Meta:
        verbose_name ='Преподаватель'
        verbose_name_plural='Преподаватели'


    def __str__(self):
        return self.name


class Course(models.Model):
    """'Модель Курсов"""
    name = models.CharField(max_length=100,verbose_name='Названия курса')

    slug = models.SlugField(max_length=100,unique=True)

    info = models.TextField(verbose_name='Информация о курсе')

    teacher = models.ForeignKey(to=Teacher,on_delete=models.RESTRICT,verbose_name='Преподаватель')

    duration = models.CharField(max_length=100,verbose_name='Длительность занятий')

    price = models.CharField(max_length=100,verbose_name='Стоимость курса')

    age_category = models.CharField(max_length=100,verbose_name='Возрастная категория')

    image = models.ImageField(default='images/default.png',
                              validators=[FileExtensionValidator(['jpg','png','jpeg','webp'])],
                              upload_to='images/%Y/%m',
                              null = True,
                              blank = True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name ='Курс'
        verbose_name_plural='Курсы'


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'slug':self.slug})


