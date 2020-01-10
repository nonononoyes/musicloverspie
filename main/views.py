from django.shortcuts import render
from django.http import HttpResponse
from .selenium import replaceKey

def index(request):
    return render(request, "index.html")

def replace(request):
    key = request.POST.get('key','')
    print (key)

    content = replaceKey(key)
    print(content)
    return HttpResponse(content)