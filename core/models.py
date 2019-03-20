from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

# Create your models here.

# ForeignKey is stored as an empty string automatically in the database, so null=True is not needed!

class User(AbstractUser):
    '''Model represents the user's post'''
    username = models.CharField(max_length=15, unique=True, null=False, blank=False)
    # Can a model have a relationship to a form?
    # profile_picture = models.OneToOne(null=True, blank=True)
    slug = models.SlugField()
    voted = models.ForeignKey('Vote', null=True, blank=True, on_delete = models.SET_NULL)
    email = models.CharField(max_length=50, null=False, blank=False)
    gender_pronouns = models.CharField(max_length=15, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, blank=True)
    about = models.TextField(max_length=1000, null=True, blank=True)


class UserPost(models.Model):
    '''Model represents the user's posts'''
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, help_text='What is your post called?', null=False)
    source_name = models.URLField(help_text='Please enter the base domain of your link, i.e., "cnn.com" or "www.google.com."',null=True, blank=True)
    post_url = models.URLField(null=True, blank=True)
    time_posted = models.DateTimeField(auto_now_add=True, blank=True)
    body = models.TextField(max_length=1000, null=True, blank=True)
    topic = models.ManyToManyField('Topic', related_name='posts')
    slug = models.SlugField()
    votes = models.ForeignKey('Vote', null=True, blank=True, on_delete = models.SET_NULL)
    comments = models.ForeignKey('Comment', null=True, blank=True, on_delete = models.SET_NULL)

    # Can we sort via a ForeginKeyField?
    class Meta:
        ordering = ['votes']

    def set_slug(self):
        '''Creates a unique slug for every post'''
        if self.slug:
            return
        base_slug = slugify(self.title)

        slug = base_slug
        n = 0

        while UserPost.object.filter(slug=slug).count():
            n += 1
            slug = base_slug + '-' + str(n)
        
        self.slug = slug

    def save(self, *args, **kwargs):
        '''Hides slug field in admin'''
        self.set_slug()
        super().save(*args, **kwargs)

class Vote(models.Model):
    '''Model represents votes on a post'''
    
    pass
    
class Comment(models.Model):
    pass

class Topic(models.Model):
    pass

