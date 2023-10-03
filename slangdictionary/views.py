from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Slang

# Create your views here.

# slangs = [ 
#     {'id':1, 'name':'Abuden', 'definition':'Means to reply sarcastically in “what else did you expect”.'},
#     {'id':2, 'name':'Aduh/Aiya', 'definition':'To convey annoyance, suffering, or pain experienced.'},
#     {'id':3, 'name':'Ang Moh', 'definition':'Describes Caucasians.'},

# ]

@login_required(login_url='login')
def slangdictionary(request):
    slangs = Slang.objects.all()
    context = {'slangs': slangs}
    return render(request, 'slangdictionary/slangdictionary.html', context)