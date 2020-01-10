from django.contrib.auth.forms import UserCreationForm

from users.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'iban', 'role', 'password1', 'password2']
