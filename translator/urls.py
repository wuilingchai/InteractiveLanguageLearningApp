from django.urls import path
from . import views, api

urlpatterns = [
    path("translator/", views.translator, name="translator"),
    path('translator/api/translation-history/', api.translation_history_list, name='translation-history-list'),
    path('translator/api/translate/', api.perform_translation, name='perform-translation'),
]