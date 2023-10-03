from django.urls import path
from . import views

urlpatterns =[
    path('quiz/', views.quiz, name="quiz"),
    path('mixmatch/', views.mixmatch, name="mixmatch"),
    path('dialogchoice/', views.dialogchoice, name="dialogchoice"),


]