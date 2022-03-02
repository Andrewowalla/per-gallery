from tkinter import image_names
from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod   
    def update_location(cls, id, name):
        cls.objects.filter(id=id).update(name=name)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    @classmethod
    def search_by_category(cls, search_term):
        category = cls.objects.filter(name_icontains=search_term)
        return category

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod   
    def update_category(cls, id, name):
        cls.objects.filter(id=id).update(name=name)


    def __str__(self):
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


    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id ,image, image_description , name,image_category,image_location):
        cls.objects.filter(id = id).update(image=image,image_description=image_description,name=name,image_category=image_category,image_location=image_location)

    @classmethod
    def search_by_category(cls, search_term):
        category = cls.objects.filter(name_icontains=search_term)
        return category

    @classmethod
    def get_all(cls):
        image = cls.objects.all()
        return image
  
    @classmethod
    def filter_by_location(cls,location):
        image = cls.objects.filter(location__name=location)
        return image

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id=id).all()
        return image
