from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from . import forms


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect('/')
        else:
            args = {'form': form}
            return render(request, 'pages/register.html', args)
    else:
        form = forms.RegistrationForm()
        args = {'form': form}
        return render(request, 'pages/register.html', args)


@login_required
def index(request):
    return render(request, 'pages/index.html')
