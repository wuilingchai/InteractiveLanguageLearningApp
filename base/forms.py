from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from .models import User

# These no need, because you use your own User Model, if you import this from the bottom you will use the django default one
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model

# User = get_user_model()

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("The two password fields didn't match."))
        
        return password2


class UserForm(ModelForm):
    class Meta:
        model = User
        # typo also is fields not field
        fields = ['username', 'email']
        # fields = ['avatar', 'name', 'username', 'email']