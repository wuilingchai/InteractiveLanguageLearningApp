from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import WordMatchForm
from .models import Word, Choices 
from learningmodule.models import Vocabulary, Pharmacy, Restaurant, Airport, Teatime, Transportation, Direction





# Create your views here.
@login_required(login_url='login')
def quiz(request):
    return render(request, 'quiz/quiz.html')

@login_required(login_url='login')
def mixmatch(request):
    words = Word.objects.all()
    return render(request, 'quiz/mixmatch.html', {'words':words})

@login_required(login_url='login')
def dialogchoice(request):
    pharmacys = Pharmacy.objects.all()
    restaurants = Restaurant.objects.all()
    airport = Airport.objects.all()
    transportation = Transportation.objects.all()
    teatime = Teatime.objects.all()
    direction = Direction.objects.all()
    context = {'pharmacys':pharmacys, 'restaurants': restaurants, 'airport': airport, 'transporation': transportation, 'teatime':teatime, 'direction': direction}

    return render(request, 'quiz/dialogchoice.html', context)