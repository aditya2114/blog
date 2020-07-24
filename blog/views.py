from django.shortcuts import render
from .models import pythonproject, webdevproject, mlproject

# Create your views here.
def pythonprojects(request):
    posts = pythonproject.objects.all().order_by('-date')
    context = {'posts': posts}
    return render(request, 'blog/pythonprojects.html', context)

def webdev(request):
    posts = webdevproject.objects.all().order_by('-date')
    context = {'posts': posts}
    return render(request, 'blog/webdev.html', context)

def mlprojects(request):
    posts = mlproject.objects.all().order_by('-date')
    context = {'posts': posts}
    return render(request, 'blog/mlprojects.html', context)

def pythonposts(request,slug):
    post = pythonproject.objects.filter(slug=slug).first()
    context = {'post': post}
    return render(request, 'blog/pythonposts.html',context)

def webdevposts(request, slug):
    post = webdevproject.objects.filter(slug=slug).first()
    context = {'post': post}
    return render(request, 'blog/webdevposts.html', context)

def mlprojectsposts(request, slug):
    post = mlproject.objects.filter(slug=slug).first()
    context = {'post': post}
    return render(request, 'blog/mlposts.html', context)
