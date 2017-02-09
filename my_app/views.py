from django.shortcuts import render
from django.http import HttpResponse

def hello(request, number):
    return HttpResponse("Hello, world. yesyes")
# Create your views here.
