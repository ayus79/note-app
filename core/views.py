from django.shortcuts import render, redirect
from django.http import HttpResponse,request
from core.models import Blog

# Create your views here.
def homepage(request):
    blog = Blog.objects.all()
    context = {
        'data': blog
    }
    return render(request, 'index.html', context)

def add(request):
    if request.method == "POST":
        title = request.POST.get('title')
        para = request.POST.get('para')
        blog = Blog(
            title = title,
            para = para
        )
        blog.save()
    return redirect('index')

def updatepage(request, id):
    blog = Blog.objects.filter(id = id)
    context = {
        'data': blog
    }
    return render(request, 'update.html', context)

def update(request, id):
    if request.method == "POST":
        title = request.POST.get('title')
        para = request.POST.get('para')
        blog = Blog(
            id = id,
            title = title,
            para = para
        )
        blog.save()
    return redirect('index')

def delete(request, id):
    blog = Blog.objects.filter(id = id).delete()
    return redirect('index')