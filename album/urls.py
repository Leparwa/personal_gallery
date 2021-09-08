from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all-photos', views.all_photos, name='photos'),
    path('new-photo', views.add_photo, name='photo'),
    path('category', views.search_image_by_category, name='search_category'),
    path('location', views.filter_by_location, name='filter_location'),
    path('view/<int:id>', views.get_image_id, name='photo'),
]