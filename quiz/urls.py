from django.urls import path
from . import views, api

urlpatterns =[
    path('quiz/', views.quiz, name="quiz"),
    path('mixmatch/', views.mixmatch, name="mixmatch"),
    path('dialogchoice/', views.dialogchoice, name="dialogchoice"),
    path('quiz/api/choices/', api.ChoicesListAPIView.as_view(), name='choices-list'),
    path('quiz/api/validate-answer/', api.ValidateAnswerAPIView.as_view(), name='validate-answer'),


]