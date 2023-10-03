from django.urls import path
from . import views

urlpatterns = [
    path("learningmodule/", views.learningmodule, name="learningmodule"),
    path("vocabulary/", views.vocabulary, name="vocabulary"),
    path("scenariobased/", views.scenariobased, name="scenariobased"),
    path("pharmacy/", views.pharmacy, name="pharmacy"),
    path("restaurant/", views.restaurant, name="restaurant"),
    path("airport/", views.airport, name="airport"),
    path("teatime/", views.teatime, name="teatime"),
    path("transportation/", views.transportation, name="transportation"),
    path("directions/", views.directions, name="directions"),


]