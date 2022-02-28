from tkinter import image_names
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)

    def __string__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __string__(self):
        return self.name

class Image(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length= 100)
    image_description = models.TextField()
    image_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category, on_delete=models.CASCADE)

class tags(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name