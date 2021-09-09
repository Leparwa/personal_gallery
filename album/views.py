from django.http.response import Http404
from django.core.exceptions import ObjectDoesNotExist
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
            print(data.image.url)
            Image(image= data.image.url, name= data.name, description= data.description,  category = data.category,  location= data.location)
            return redirect('photos')
    else:
        form = ImageForm()
    return render(request, 'all_photos/image.html', {'form': form})

def search_image_by_category(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"
        return render(request, 'all_photos/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all_photos/search.html',{"message":message})

def filter_by_location(request):
    if 'location' in request.GET and request.GET["location"]:
        search_term = request.GET.get("location")
        searched_images = Image.filter_by_location(search_term)
        message = f"{search_term}"
        return render(request, 'all_photos/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all_photos/search.html',{"message":message})


def get_image_id(request, id):
    try:
        image = Image.get_image_by_id(id)
    except Image.DoesNotExist:
        raise Http404()
    return render(request, 'all_photos/modal_view.html', {"image":image})


