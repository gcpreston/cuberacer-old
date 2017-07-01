from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from . import forms


def register(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = forms.RegistrationForm()
            args = {'form': form}
            return render(request, 'pages/register_failed.html', args)
    else:
        form = forms.RegistrationForm()
        args = {'form': form}
        return render(request, 'pages/register.html', args)


@login_required
def index(request):
    return render(request, 'pages/index.html')
