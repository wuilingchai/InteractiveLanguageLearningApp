from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import WordMatchForm
from .models import Word


# Create your views here.
@login_required(login_url='login')
def quiz(request):
    return render(request, 'quiz/quiz.html')

@login_required(login_url='login')
def mixmatch(request):
    words = Word.objects.all()
    feedback_message = None  # Initialize feedback message

    if request.method == 'POST':
        form = WordMatchForm(request.POST)
        if form.is_valid():
            # Check if the user's match is correct
            original_word = form.cleaned_data['original_word']
            match_word = form.cleaned_data['match_word']
            correct_match = Word.objects.filter(original_word=original_word, match_word=match_word).exists()
            
            if correct_match:
                # Handle correct match by displaying a success message
                feedback_message = "Correct match! Well done!"
            else:
                # Handle incorrect match by displaying an error message
                feedback_message = "Incorrect match. Try again!"

    else:
        form = WordMatchForm()

    context = {
        'words': words,
        'form': form,
        'feedback_message': feedback_message,  # Pass the feedback message to the template
    }
    return render(request, 'quiz/mixmatch.html', context)

@login_required(login_url='login')
def dialogchoice(request):
    return render(request, 'quiz/dialogchoice.html')