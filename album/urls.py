from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all-photos', views.all_photos, name='photos'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]