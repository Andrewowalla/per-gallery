from unicodedata import category
from django.test import TestCase
from .models import Location, Category,tags,Image

# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.andrew = Location(name='kenya')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.andrew,Location))
 
    def test_save_method(self):
        self.andrew.save_location()
        name = Location.objects.all()
        self.assertTrue(len(name)>0)   

class CategoryTestClass(TestCase):
    def setUp(self):
        self.andrew = Category(name='Travel')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.andrew,Category))   
        
    def test_save_method(self):
        self.andrew.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)

class ImageTestClass(TestCase):
    def setUp(self):
        self.andrew = Image(image='Picnic')

    def test_instance(self):
        self.assertTrue(isinstance(self.andrew,Image))

    def test_save_method(self):
        self.andrew.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)                  