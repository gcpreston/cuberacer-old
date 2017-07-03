from django.http import HttpResponse
from django.shortcuts import render


def solo(request):
    if request.method == 'POST':
        print(request.POST.get('value1'))
        return HttpResponse(status=201)
    else:
        return render(request, 'timer/solo.html')


def multi(request):
    return render(request, 'timer/multi.html')
