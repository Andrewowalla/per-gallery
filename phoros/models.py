from tkinter import image_names
from django.db import models
import datetime as dt
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

class tags(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Image(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length= 100)
    image_description = models.TextField()
    tags = models.ManyToManyField(tags)
    image_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.image

    def save_image(self):
        self.save()

    @classmethod
    def search_by_category(cls, search_term):
        image = cls.objects.filter(category__name__icontains=search_term)
        return image 