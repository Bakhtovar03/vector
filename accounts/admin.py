from uuid import uuid4

from django.contrib import admin
from django.contrib.auth.models import User
from pytils.translit import slugify

from .models import UserProfile



@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ('bio',)
    search_fields = ('user','bio')
    exclude = ['slug']

    def save_model(self, request, obj, form, change):
        obj.slug = f'{slugify(obj.user)}-{uuid4().hex[:4]}'
        super().save_model(request, obj, form, change)
