from django.shortcuts import render
from django.http import HttpResponse


def about(request):
    return render(request, 'main1/about.html')

def index(request):
    return render(request, 'main1/index.html')
 