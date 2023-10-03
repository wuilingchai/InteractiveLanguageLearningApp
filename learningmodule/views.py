from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Vocabulary


vocabulary = [ 
    {'id':1, 'name':'Abuden', 'definition':'Means to reply sarcastically in “what else did you expect”.'},
    {'id':2, 'name':'Aduh/Aiya', 'definition':'To convey annoyance, suffering, or pain experienced.'},
    {'id':3, 'name':'Ang Moh', 'definition':'Describes Caucasians.'},

]
# Create your views here.
@login_required(login_url='login')
def learningmodule(request):
    return render(request, 'learningmodule/learningmodule.html')

@login_required(login_url='login')
def vocabulary(request):
    vocabularys = Vocabulary.objects.all()
    context = {'vocabularys':vocabularys}
    return render(request, 'learningmodule/vocabulary.html', context)

@login_required(login_url='login')
def scenariobased(request):
    return render(request, 'learningmodule/scenariobased.html')


@login_required(login_url='login')
def pharmacy(request):
    return render(request, 'learningmodule/pharmacy.html')

@login_required(login_url='login')
def restaurant(request):
    return render(request, 'learningmodule/restaurant.html')

@login_required(login_url='login')
def airport(request):
    return render(request, 'learningmodule/airport.html')

@login_required(login_url='login')
def teatime(request):
    return render(request, 'learningmodule/teatime.html')

@login_required(login_url='login')
def transportation(request):
    return render(request, 'learningmodule/transportation.html')

@login_required(login_url='login')
def directions(request):
    return render(request, 'learningmodule/directions.html')