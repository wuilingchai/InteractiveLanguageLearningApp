from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User

# These no need, because you use your own User Model, if you import this from the bottom you will use the django default one
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model

# User = get_user_model()

class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('avatar', 'name')
        # ['avatar', 'name', 'username', 'email', 'password1', 'password2']

class UserForm(ModelForm):
    class Meta:
        model = User
        # typo also is fields not field
        fields = ['username', 'email']
        # fields = ['avatar', 'name', 'username', 'email']