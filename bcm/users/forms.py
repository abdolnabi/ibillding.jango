from django.contrib.auth.forms import UserCreationForm
from django import forms
from users.models import User
from django.utils.translation import ugettext as _


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'iban', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(label=_('Username'))
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
