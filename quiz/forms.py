
from django import forms
from .models import Word

class WordMatchForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['original_word', 'match_word']
