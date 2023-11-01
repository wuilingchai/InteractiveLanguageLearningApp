from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Vocabulary, Pharmacy, Restaurant, Airport, Teatime, Transportation, Direction
from .form import VocabularySearchForm



# vocabulary = [ 
#     {'id':1, 'name':'Abuden', 'definition':'Means to reply sarcastically in “what else did you expect”.'},
#     {'id':2, 'name':'Aduh/Aiya', 'definition':'To convey annoyance, suffering, or pain experienced.'},
#     {'id':3, 'name':'Ang Moh', 'definition':'Describes Caucasians.'},

# ]
# Create your views here.
@login_required(login_url='login')
def learningmodule(request):
    return render(request, 'learningmodule/learningmodule.html')

@login_required(login_url='login')
def vocabulary(request):
    form = VocabularySearchForm(request.GET)
    query = request.GET.get('search')
    vocabularys = Vocabulary.objects.all()
    context = {'vocabularys':vocabularys, 'form':form}

    if query:
        vocabularys = vocabularys.filter(name__icontains=query)

    return render(request, 'learningmodule/vocabulary.html', context)

@login_required(login_url='login')
def scenariobased(request):
    return render(request, 'learningmodule/scenariobased.html')


@login_required(login_url='login')
def pharmacy(request):
    pharmacys = Pharmacy.objects.all()
    context = {'pharmacys':pharmacys}
    print(dict(request.POST.items()))
    print(pharmacys)

    return render(request, 'learningmodule/pharmacy.html', context)

@login_required(login_url='login')
def restaurant(request):
    restaurants = Restaurant.objects.all()
    context = {'restaurants':restaurants}
    print(dict(request.POST.items()))
    print(restaurants)

    return render(request, 'learningmodule/restaurant.html', context)

@login_required(login_url='login')
def airport(request):
    airports = Airport.objects.all()
    context = {'airports':airports}
    print(dict(request.POST.items()))
    print(airports)
    return render(request, 'learningmodule/airport.html', context)

@login_required(login_url='login')
def teatime(request):
    teatimes = Teatime.objects.all()
    context = {'teatimes':teatimes}
    print(dict(request.POST.items()))
    print(teatimes)
    return render(request, 'learningmodule/teatime.html', context)

@login_required(login_url='login')
def transportation(request):
    transportations = Transportation.objects.all()
    context = {'transportations':transportations}
    print(dict(request.POST.items()))
    print(transportations)
    return render(request, 'learningmodule/transportation.html', context)

@login_required(login_url='login')
def directions(request):
    directions = Direction.objects.all()
    context = {'directions':directions}
    print(dict(request.POST.items()))
    print(directions)
    return render(request, 'learningmodule/directions.html', context)