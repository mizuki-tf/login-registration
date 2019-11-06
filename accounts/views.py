from django.urls import reverse_lazy
from django.views import generic
from .forms import LoginForm,UserCreateForm
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (LoginView, LogoutView)

User = get_user_model()

class Top(generic.TemplateView):
    template_name = 'top.html'

class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'

class LogoutView(LogoutView,LoginRequiredMixin):
    template_name = 'top.html'

class SignUpView(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('accounts:top')
    template_name = 'registration/signup.html'
