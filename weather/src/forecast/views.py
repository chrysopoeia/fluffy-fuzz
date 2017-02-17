from django import forms

from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)


class Register(CreateView):
    template_name = 'forecast/register.html'
    form_class = UserRegistrationForm
    success_url = ''


class Home(TemplateView):
    template_name = 'forecast/home.html'
