from django.shortcuts import render, redirect

from django.views import generic

from django.urls import reverse_lazy

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserUpdateForm, ProfileUpdateForm


class RegisterView(SuccessMessageMixin, generic.CreateView):
    from .models import User
    from .forms import UserRegisterForm

    model = User
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('blog-home')
    success_message = "Congrats! You can now login with %(username)s."


@login_required
def profile(request):
    # It's complex to handle 2 forms with classed based view so going for function based view.
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
