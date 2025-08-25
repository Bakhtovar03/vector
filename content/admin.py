from django.contrib import admin

from content.models import Teacher, Course


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
