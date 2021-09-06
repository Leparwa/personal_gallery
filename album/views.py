from django.shortcuts import redirect, render, resolve_url
from django.http import HttpResponse
from .models import Image, Category, Location
import datetime as dt


def index(request):
    date = dt.date.today()
    return redirect('photos')
    # return render(request, 'all_photos/base.html',{"title":"gallery","date":date})
def all_photos(request):
    all_photos = Image.objects.all()
    category = Category.objects.all()
    return render(request, 'all_photos/photos.html',{"title":"photos", "photos":all_photos, "category":category})


