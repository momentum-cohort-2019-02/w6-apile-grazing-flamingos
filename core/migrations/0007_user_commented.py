# Generated by Django 2.1.7 on 2019-03-22 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_DataMigrate'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='commented',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='writer', to='core.Comment'),
        ),
    ]