from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
# Create your views here.

def home(request):
    context = {
        "posts":Posts.objects.all(),
        "title":"Home"
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{"title":"About"})

