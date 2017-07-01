from django.http import HttpResponse
from django.shortcuts import render


def solo(request):
    return HttpResponse('Solo')


def multi(request):
    return HttpResponse('Multi')
