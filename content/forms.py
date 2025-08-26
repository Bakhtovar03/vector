from django import forms
from .models import Course
from phonenumber_field.formfields import PhoneNumberField

class SubscribeForm(forms.Form):
    CONTACT_CHOICES = (
        ('vk', 'VK'),
        ('telegram', 'Telegram'),
        ('phone', 'Контактный телефон'),
    )

    name = forms.CharField(
        max_length=100,
        help_text='Ваше ФИО',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    children_name = forms.CharField(
        max_length=100,
        help_text='ФИО ребёнка',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    children_age = forms.IntegerField(
        max_value=17,
        min_value=0,
        help_text='Возраст ребенка',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    contact_method = forms.MultipleChoiceField(
        choices=CONTACT_CHOICES,
        label='Способы связи',
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'})
    )

    contact = PhoneNumberField(
        help_text='Номер для связи',
        widget=forms.TextInput(attrs={'type': 'tel', 'class': 'form-control'})
    )

    vk_url = forms.URLField(
        help_text='Ссылка на вашу страничку в ВК при наличии',
        required=False,
        widget=forms.URLInput(attrs={'class': 'form-control'})
    )