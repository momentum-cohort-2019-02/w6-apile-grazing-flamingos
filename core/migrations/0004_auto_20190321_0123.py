# Generated by Django 2.1.7 on 2019-03-21 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190320_1343'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userpost',
            options={'ordering': ['-time_posted']},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.TextField(blank=True, max_length=1200, null=True, verbose_name='kind words'),
        ),
        migrations.AddField(
            model_name='topic',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='topic',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='profile_pictures'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender_pronouns',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
