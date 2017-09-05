from django.http import HttpResponse
from django.shortcuts import render

def helloWorld(request):
    return HttpResponse('Witaj świecie :)')
