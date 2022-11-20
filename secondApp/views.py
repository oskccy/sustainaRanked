from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mainPage(request):
    s='Response'
    return HttpResponse(s)





