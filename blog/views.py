from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Hello world')