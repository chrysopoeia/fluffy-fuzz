from django.views.generic import CreateView, FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import logout, login
from .forms import RegistrationForm, LoginForm


class Register(CreateView):
    template_name = 'account/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')


class Login(FormView):
    template_name = 'account/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('forecast')
    
    def form_valid(self, form, *args, **kwargs):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form, *args, **kwargs)


class Logout(TemplateView):
    template_name = 'account/logout.html'
    
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super(Logout, self).dispatch(request, *args, **kwargs)
