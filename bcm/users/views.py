from django.shortcuts import render
from django.utils.translation import gettext
from django.utils import translation
from users.forms import SignUpForm


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})
