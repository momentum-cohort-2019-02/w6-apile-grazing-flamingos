# Generated by Django 2.1.7 on 2019-03-20 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='What is your post called?', max_length=100)),
                ('source_name', models.URLField(blank=True, help_text='Please enter the base domain of your link, i.e., "cnn.com" or "www.google.com."', null=True)),
                ('post_url', models.URLField(blank=True, null=True)),
                ('time_posted', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField(blank=True, max_length=1000, null=True)),
                ('slug', models.SlugField()),
                ('comments', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Comment')),
                ('topic', models.ManyToManyField(related_name='posts', to='core.Topic')),
            ],
            options={
                'ordering': ['votes'],
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='about',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='date_created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='gender_pronouns',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AddField(
            model_name='userpost',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userpost',
            name='votes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Vote'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='voted',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Vote'),
        ),
    ]
