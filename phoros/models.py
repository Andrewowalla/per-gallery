from tkinter import image_names
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Image(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length= 30)
    image_description = models.TextField()
    image_location = models.ForeignKey( on_delete=models.CASCADE)
    image_category = models.ForeignKey( on_delete=models.CASCADE)