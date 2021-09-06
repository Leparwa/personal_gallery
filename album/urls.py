from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all-photos', views.all_photos, name='photos'),
    path('new-photo', views.add_photo, name='photo'),
]