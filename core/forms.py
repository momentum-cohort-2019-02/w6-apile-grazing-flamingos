from django.forms import ModelForm
from core.models import User

class UserForm(ModelForm):
    """
    User profile form based on our User model. Asks for User input on specified fields
    """
    class Meta:
        model = User
        fields = ['username', 'email', 'gender_pronouns', 'about',]
