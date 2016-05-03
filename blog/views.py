from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from blog.models import Blog


def index(request):
    """Blog list"""
    blogs = Blog.objects.all()
    for b in blogs:
        b.content = b.content[:150]
    return render(request, 'index.html', {'blogs': blogs})

def show(request, *args):
    blog_id = args[0]
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'index.html', {'blog': blog})