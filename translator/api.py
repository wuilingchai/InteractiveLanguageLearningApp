from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import TranslationHistory
from .serializer import TranslationHistorySerializer
from googletrans import Translator

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def translation_history_list(request):
    history = TranslationHistory.objects.filter(user=request.user)
    serializer = TranslationHistorySerializer(history, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def perform_translation(request):
    text = request.data.get("translate")
    to_lang = request.data.get("tolanguage")
    from_lang = request.data.get("fromlanguage")
    
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

    return Response({"translation": translation.text})
