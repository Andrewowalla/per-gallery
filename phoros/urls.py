from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.index, name = 'index'),
    path('search/',views.search_results,name='search_results'),
    path('category/', views.category, name='category'),
    path('image/<int:image_id>/',views.get_image_by_id, name ='get_image_by_id'),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)