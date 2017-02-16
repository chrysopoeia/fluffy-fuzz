from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, TemplateView


class Register(CreateView):
    template_name = 'forecast/register.html'
    form_class = UserCreationForm
    success_url = ""


class Home(TemplateView):
    template_name = 'forecast/home.html'
