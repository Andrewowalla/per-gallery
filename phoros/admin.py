from django.contrib import admin
from . models import Location, Category, tags, Image

# Register your models here.

admin.site.register(Location)
admin.site.register(Category)
admin.site.register(tags)
admin.site.register(Image)