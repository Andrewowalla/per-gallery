from email.mime import image
from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

from phoros.models import Location, Category, Image

# Create your views here.
def index(request):
    location = Location.objects.all() 
    category = Category.objects.all()
    image  = Image.objects.all()
    
    return render(request, 'index.html', {"loaction":location, "category":category, "image":image})

def search_results(request):
  
  if 'image' in request.GET and request.GET["image"]:
    search_term = request.GET.get("image")
    searched_images = Image.search_by_category(search_term)
    message = f"{search_term}"
    
    return render(request,"search.html", {'message':message,'images':searched_images})
  else:
    message = "Please input a valid term"
    return render(request,'search.html', {'message':message})