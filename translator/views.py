from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from googletrans import Translator
from .models import TranslationHistory

# Create your views here.
@login_required(login_url='login')
def translator(request):
    if request.method == "POST":
        text = request.POST["translate"]
        to_lang = request.POST["tolanguage"]
        from_lang = request.POST["fromlanguage"]

        translator = Translator()

        translation = translator.translate(text, src=from_lang, dest=to_lang)

        translation_history = TranslationHistory(
            user=request.user,
            source_text=text,
            source_language=from_lang,
            trans_text=translation.text,
            trans_language=to_lang,
        )
        translation_history.save()

        translation_history = TranslationHistory.objects.filter(user=request.user)
 
        context = {
            'translation': translation.text,
            'translation_history': translation_history,
        }

        return render(request, 'translator/translator.html', context)
    return render(request, 'translator/translator.html')


