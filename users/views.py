from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


class RegisterView(SuccessMessageMixin, generic.CreateView):
    from .models import User
    from .forms import UserRegisterForm

    model = User
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('blog-home')
    success_message = "Congrats! You can now login with %(username)s."
