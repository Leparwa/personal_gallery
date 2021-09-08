from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all-photos', views.all_photos, name='photos'),
    path('new-photo', views.add_photo, name='photo'),

    path('search', views.search_image_by_category, name='search_category'),
    path('search', views.filter_by_location, name='filter_location'),
]