from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('name', 'avatar')
        # ['avatar', 'name', 'username', 'email', 'password1', 'password2']

class UserForm(ModelForm):
    class Meta:
        model = User
        field = ['username', 'email']
        # fields = ['avatar', 'name', 'username', 'email']