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

    def test_delete_method(self):
        self.andrew.delete_location()
        name = Location.objects.all()
        self.assertTrue(len(name)>0)

    def test_update_location(self):
        self.andrew.save_location()
        self.andrew.update_location(self.andrew.id, location)    
        location = Location.objects.filter(name='Botswana')
        self.assertTrue(len(location)>0)
    
class CategoryTestClass(TestCase):
    def setUp(self):
        self.andrew = Category(name='Travel')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.andrew,Category))   
        
    def test_save_method(self):
        self.andrew.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)

    def test_delete_method(self):
        self.andrew.save_category()
        self.andrew.delete_category()
        search_category = Category.objects.all()
        self.assertTrue(len(search_category) == 0)

    def test_update_category(self):
        self.andrew.save_category()
        self.andrew.update_category(self.andrew.id, category)    
        category = Category.objects.filter(name='Wildlife')
        self.assertTrue(len(category)>0)

class ImageTestClass(TestCase):
    def setUp(self):
        self.andrew = Location(name='South Africa')
        self.andrew.save_location()

        self.andrew = Category(name='Food')
        self.andrew.save_category()

        self.andrew = Image(image='tou.jpg',category=self.andrew,location=self.andrew)
        self.andrew.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.andrew,Image))        
        
    def test_save_method(self):
        self.andrew.save_image()
        image = Image.objects.all()
        self.assertTrue(len(image)>0)             

    def test_delete_image(self):
        self.andrew.delete_image()
        image = Image.objects.all()
        self.assertTrue(len(image)==0)

        self.assertTrue(len(image)==0)

    def test_update_image(self):
        self.andrew.save_image()
        self.andrew.update_image(self.andrew.id,'tou.jpg')    
        image = Image.objects.filter(image='tou.jpg')
        self.assertTrue(len(image)>0)

    def test_get_image_by_id(self):
        image=self.andrew.get_image_by_id(self.andrew.id)
        image=Image.objects.filter(id=self.andrew.id)    
        self.assertTrue(image.query,image.query)

    def tearDown(self):
        Image.objects.all().delete()
        Category.objects.all().delete()     