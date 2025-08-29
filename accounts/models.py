from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class UserProfile(models.Model):
    slug = models.SlugField(unique=True)
    bio = models.TextField(blank=True, help_text='Дополнительная информация')
    date_of_birth = models.DateField(null=True, blank=True, help_text="Дата рождения")

    avatar = models.ImageField(upload_to="avatars/%Y%m", default="avatars/default.png",
                               validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

    def __str__(self):
        return f'profile-{self.user.username}'

    def get_absolute_url(self):
        return reverse('profile', kwargs={'slug': self.slug})

