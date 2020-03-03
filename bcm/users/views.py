from django.shortcuts import render
from django.shortcuts import render, redirect
from users.forms import SignUpForm


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
        return redirect('users:login')


    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})
