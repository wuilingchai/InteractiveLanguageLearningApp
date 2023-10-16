from rest_framework import generics, status
from rest_framework.response import Response
from .models import Choices
from .serializer import ChoicesSerializer

class ChoicesListAPIView(generics.ListAPIView):
    queryset = Choices.objects.all()
    serializer_class = ChoicesSerializer

class ValidateAnswerAPIView(generics.GenericAPIView):
    serializer_class = ChoicesSerializer

    def post(self, request, *args, **kwargs):
        question_id = request.data.get('id')
        selected_answer = request.data.get('answer')

        try:
            question = Choices.objects.get(pk=question_id)
        except Choices.DoesNotExist:
            return Response({"error": "Question not found."}, status=status.HTTP_404_NOT_FOUND)

        if selected_answer == question.answer:
            return Response({"result": "Correct"})
        else:
            return Response({"result": "Incorrect"})
