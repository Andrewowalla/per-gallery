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

def location(request,location):
    image=Image.objects.filter(location=location)

    return render(request,'location.html',{"image":image})

def category(request,category):

    category = Category.objects.all()
    image=Image.objects.filter(category=category)

    return render(request,'category.html',{"category":category, "image":image})

def search_results(request):
  
  if 'category' in request.GET and request.GET["category"]:
    search_term = request.GET.get("category")
    searched_category = Category.search_by_category(search_term)
    message = f"{search_term}"
    
    return render(request,"search.html", {'message':message,'category':searched_category})
  else:
    message = "Please input a valid category"
    return render(request,'search.html', {'message':message})


def get_image_by_id(request,image_id):
  try:
    image= Image.objects.get(id=image_id)
  except:
    raise Http404()  
  return render(request,'display.html',{'image':image})

def filter_by_location(request,location):
  image= Image.filter_by_location(location)
  
  return render(request,'location.html',{'image':image})