from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
import datetime as dt


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    date = dt.date.today()
    return render(request, 'all_photos/base.html',{"title":"gallery","date": date})
def all_photos(request):
    return render(request, 'all_photos/photos.html',{"title":"photos"})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)