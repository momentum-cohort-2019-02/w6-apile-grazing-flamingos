# Generated by Django 2.1.7 on 2019-03-22 04:54
import os.path, csv
from django.conf import settings
from django.core.files import File
from django.db import migrations
from django.utils.text import slugify
# from django.db.models import Count, IntegerField

def get_apile_csv(apps, schema_editor):
    """Read CSV file with user and post data and insert them into DB"""
    # User = apps.get_model('core', 'User')
    # UserPost = apps.get_model('core', 'UserPost')
    # Comment = apps.get_model('core', 'Comment')
    # Topic = apps.get_model('core', 'Topic')
    # Vote = apps.get_model('core', 'Vote')
    # datapath = os.path.join(settings.BASE_DIR, 'initial_data')
    # datafile = os.path.join(datapath, 'ApileData3.csv')

    # with open(datafile) as file:
    #     reader = csv.DictReader(file)
    #     for row in reader:
    #     # Not sure if I need the 'if' statement we used in the book example  tbh... 
    #     # Is that to make sure we only run this loop if there is new data? 
    #     # Anyways, not including the `if UserPost.objects.filter()....`

    #         user, _ = User.objects.get_or_create(
    #             username=row['name'],
    #             gender_pronouns=row['gender_pronouns'],
    #             email=row['email'],
    #         )
    #         user.slug = slugify(user.username)[:49]
    #         user.save()

    #         topic, _ = Topic.objects.get_or_create(
    #             name=row['topic'],
    #         )
    #         # Had to put topic.slug outside of topic so we can call 'topic.name' in slugify function. 
    #         # BUT it should still be ok bc we are using get_or_create for the topic name so there should not be duplicates.
    #         topic.slug = slugify(topic.name)[:49]
    #         topic.save()

    #         # Do we need to use annotation here? How will this work with new votes?
    #         # https://docs.djangoproject.com/en/2.1/ref/models/database-functions/#cast   ?????
    #         vote, _ = Vote.objects.get_or_create(
    #             vote=row['votes'],
    #         )
    #         vote.save()

    #         comment, _ = Comment.objects.get_or_create(
    #             comment=row['comments'],
    #         )

    #         userpost = UserPost(
    #             user=user,
    #             title=row['title'],
    #             post_url=row['post_url'],
    #             votes=vote,
    #             comments = comment,
    #         )
    #         userpost.slug = slugify(userpost.title)[:49]
    #         userpost.save()
    #         userpost.topic.add(topic)
    #         user.userpost_set.add(userpost)
    #         topic.posts.add(userpost)
    #         vote.post.add(userpost)
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190321_1215'),
    ]

    operations = [
        migrations.RunPython(get_apile_csv),
    ]
