from django.forms import ModelForm
from core.models import User, UserPost

class UserForm(ModelForm):
    """
    User profile form based on our User model. Asks for User input on specified fields
    """
    class Meta:
        model = User
        fields = ['username', 'email', 'gender_pronouns', 'about',]

class PostForm(ModelForm):
    '''User post form based on our UserPost model. Ask'''
    class Meta:
        model = UserPost
        fields = ['title', 'source_name', 'post_url', 'body', 'topic']
