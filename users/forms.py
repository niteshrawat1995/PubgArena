from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        from django.contrib.auth.models import User

        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        from django.contrib.auth.models import User

        model = User
        fields = ('username', 'email')


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        from .models import Profile

        model = Profile
        fields = ('pubg_id', 'name', 'age', 'gender', 'image')
