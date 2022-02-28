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