from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from datetime import datetime
from django.urls import reverse


# from PIL import Image

# Create your models here.

# ForeignKey is stored as an empty string automatically in the database, so null=True is not needed!

class User(AbstractUser):
    '''Model represents the user's post'''
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
    slug = models.SlugField()
    voted = models.ForeignKey(to='Vote', null=True, blank=True, on_delete = models.SET_NULL, related_name='user')
    email = models.CharField(max_length=50, null=False, blank=False)
    gender_pronouns = models.CharField(max_length=20, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, blank=True)
    about = models.TextField(max_length=1000, null=True, blank=True)

    def set_slug(self):
        '''Creates a unique slug for every user'''
        if self.slug:
            return

    def save(self, *args, **kwargs):
        '''Hides slug field in admin- saves slug to use in url'''
        self.set_slug()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        '''Returns the url to access a particular author instance.'''
        return reverse('user-profile', args=[str(self.slug)])

    def __str__(self):
        return self.username
    

class UserPost(models.Model):
    '''Model represents the user's posts'''
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, help_text='What is your post called?', null=False)
    source_name = models.URLField(help_text='Please enter the base domain of your link, i.e., "cnn.com" or "www.google.com."', null=True, blank=True)
    post_url = models.URLField(null=True, blank=True)
    time_posted = models.DateTimeField(auto_now_add=True, blank=True)
    body = models.TextField(max_length=1000, null=True, blank=True)
    topic = models.ManyToManyField(to='Topic', related_name='posts')
    slug = models.SlugField()
    votes = models.ForeignKey(to='Vote', null=True, blank=True, on_delete = models.SET_NULL, related_name='post')
    comments = models.ForeignKey(to='Comment', null=True, blank=True, on_delete = models.SET_NULL)

    # Can we sort via a ForeginKeyField?
    class Meta:
        ordering = ['-time_posted']

    def set_slug(self):
        '''Creates a unique slug for every post'''
        if self.slug:
            return
        base_slug = slugify(self.title)

        slug = base_slug
        n = 0

        while UserPost.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + '-' + str(n)
        
        self.slug = slug

    def get_absolute_url(self):
        '''Returns the url to access a particular author instance.'''
        return reverse('index')

    def save(self, *args, **kwargs):
        '''Hides slug field in admin- saves slug to use in url'''
        self.set_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.post_url
    
    
class Comment(models.Model):
    comment = models.TextField(verbose_name='kind words', editable=True, max_length=1200, null=True, blank=True)

    def __str__(self):
        return self.comment  

class Topic(models.Model):
    slug = models.SlugField(default="")
    name = models.CharField(max_length=20, default="")

    def set_slug(self):
        '''Creates a unique slug for every topic'''
        if self.slug:
            return

    def save(self, *args, **kwargs):
        '''Hides slug field in admin- saves slug to use in url'''
        self.set_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class Vote(models.Model):
    vote = models.IntegerField(default=0)
    # user
    # post

    def __str__(self):
        return self.vote
