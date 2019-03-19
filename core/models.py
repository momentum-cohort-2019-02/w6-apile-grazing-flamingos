from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

# Create your models here.

class User(AbstractUser):
    pass

# class User_Post(models.Model):
#     '''Model represents the user's posts'''
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100, help_text='What is your post called?', null=False)
#     post_url = models.URLField(null=True, blank=True)
#     body = models.TextField(max_length=1000, null=True, blank=True)
#     topic = models.ManyToManyField('Topic', related_name='posts')
#     slug = models.SlugField()
#     votes = models.ForeignKey('Vote', on_delete = models.SET_NULL, null=True)
#     comments = models.ForeignKey('Comment', on_delete = models.SET_NULL, null=True)

#     def set_slug(self):
#         '''Creates a unique slug for every post'''
#         if self.slug:
#             return
#         base_slug = slugify(self.title)

#         slug = base_slug
#         n = 0

#         while User_Post.object.filter(slug=slug).count():
#             n += 1
#             slug = base_slug + '-' + str(n)
        
#         self.slug = slug

#     def save(self, *args, **kwargs):
#         '''Hides slug field in admin'''
#         self.set_slug()
#         super().save(*args, **kwargs)

# class Vote(models.Model):
#     pass
    
# class Comment(models.Model):
#     pass

# class Topic(models.Model):
#     pass
