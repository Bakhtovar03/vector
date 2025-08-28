from django.contrib import admin
from pytils.translit import slugify
from content.models import Teacher, Course
from uuid import uuid4

# Register your models here.
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name','subjects_taught')
    list_filter = ('subjects_taught',)
    search_fields = ('name','subjects_taught')
    ordering = ('name',)
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name','teacher','age_category')
    list_filter = ('teacher','age_category')
    search_fields = ('name','teacher','age_category')
    ordering = ('name',)

    exclude = ['slug']
    def save_model(self, request, obj, form, change):
        obj.slug = f'{slugify(obj.name)}-{uuid4().hex[:4]}'
        super().save_model(request,obj,form,change)
