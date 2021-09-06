from django.shortcuts import redirect, render, resolve_url
from django.http import HttpResponse
from .models import Image, Category, Location
import datetime as dt
from .forms import ImageForm


def index(request):
    date = dt.date.today()
    return redirect('photos')
    # return render(request, 'all_photos/base.html',{"title":"gallery","date":date})
def all_photos(request):
    all_photos = Image.objects.all()
    category = Category.objects.all()
    return render(request, 'all_photos/photos.html',{"title":"photos", "photos":all_photos, "category":category})

def add_photo(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            data = form.instance
            img_obj = Image(image= data.image.url, image_name= data.image_name, image_description= data.image_description, category = data.category, location= data.location)
            
            print(img_obj)
            return render(request, 'all_photos/image.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'all_photos/image.html', {'form': form})


