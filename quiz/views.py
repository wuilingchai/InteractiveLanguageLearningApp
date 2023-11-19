from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import WordMatchForm
from .models import Word, Choices 




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
    choices = Choices.objects.all()
    context = {'choices': choices}
    return render(request, 'quiz/dialogchoice.html', context)