from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
import datetime as dt


def index(request):
   
 
    date = dt.date.today()
    return render(request, 'all_photos/base.html',{"title":"gallery","photos": all_photos})
def all_photos(request):
    all_photos = Image.objects.all()
    return render(request, 'all_photos/photos.html',{"title":"photos", "photos":all_photos})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)