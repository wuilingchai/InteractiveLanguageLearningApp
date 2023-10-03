from django.urls import path
from . import views

urlpatterns = [
    path("slangdictionary/", views.slangdictionary, name="slangdictionary"),
]