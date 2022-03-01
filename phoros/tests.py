from django.test import TestCase
from .models import Location, Category,tags

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

