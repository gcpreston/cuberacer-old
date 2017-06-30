from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def logout_user(request):
    logout(request)
    return HttpResponse('Logged out successfully.')


@login_required
def index(request):
    return HttpResponse('Login successful.')
