from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    """
    adds an email field during registration - default field is required

    """
    email = forms.EmailField()

    class Meta:
        """
        determines how the parent class behaves
        whenever a form validates, it creates a new User model
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    """
    updates the user model's username and email
    """
    email = forms.EmailField()

    class Meta:
        """
        whenever a form validates, it updates the User model
        """
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    """
    updates the user model's image
    """
    class Meta:
        """
        whenever a form validates, it updates the User model
        """
        model = Profile
        fields = ['image']
