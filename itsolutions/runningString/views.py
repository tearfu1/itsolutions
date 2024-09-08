from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.GET:
        print(request.GET)
    return HttpResponse('page')