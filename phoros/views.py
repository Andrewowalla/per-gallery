from email.mime import image
from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import Http404
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

def get_image_by_id(request,image_id):
  try:
    image= Image.objects.get(id=image_id)
  except:
    raise Http404()  
  return render(request,'display.html',{'image':image})

def filter_by_location(request,location):
  image= Image.filter_by_location(location)
  
  
  return render(request,'location.html',{'images':image})