from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mainPage(request):
    return render(request,'homePage.html')

def competePage(request):
    return render(request, 'secondaryPage.html')

def aboutPage(request):
    return render(request, 'thirdPage.html')









