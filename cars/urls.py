from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars, name='cars'),
    path('<int:id>', views.car_details, name ='car_details',),
    path('search', views.search, name='search')
] 

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)