# forms.py
from django import forms

class VocabularySearchForm(forms.Form):
    search = forms.CharField(label='Search Vocabulary', required=False)
