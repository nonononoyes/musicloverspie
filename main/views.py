from django.shortcuts import render
from django.http import HttpResponse
import cloudscraper

def index(request):
    return render(request, "index.html")

def replace(request):
    scraper = cloudscraper.create_scraper()
    key = request.POST.get('key','')
    print (key)
    content = scraper.get("https://supgrade.eu/api?method=replace&key="+key).content
    return HttpResponse(content)