from django.shortcuts import render


def solo(request):
    return render(request, 'timer/solo.html')


def multi(request):
    return render(request, 'timer/multi.html')
