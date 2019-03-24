from django.forms import ModelForm
from core.models import User, UserPost, Comment, Topic, Vote
from django.contrib.auth.forms import UserChangeForm
# from django.contrib.auth.models import User

class EditProfileForm(UserChangeForm):
    template_name='user_profile.html'

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )

class CommentForm(ModelForm):
    """Form for users to post comments in reply to posts"""
    class Meta:
        model = Comment
        fields = ['comment',]

# class UserForm(ModelForm):
#     '''User profile form based on our User model. Asks for User input on specified fields'''
#     class Meta:
#         model = User
#         fields = ['email', 'gender_pronouns', 'about',]

class PostForm(ModelForm):
    '''User post form based on our UserPost model.'''
    class Meta:
        model = UserPost
        fields = ['title', 'source_name', 'post_url', 'body', 'topic']

class CommentForm(ModelForm):
    
    class Meta:
        model = Comment
        fields = ("comment",)

# class EditUserProfile (ModelForm):
#     '''Form that allows users to edit their profile'''
#     class Meta:
#         model = User
#         fields = ['profile_picture', 'about', 'email', 'gender_pronouns', 'about',]
