# Generated by Django 3.0.4 on 2020-03-28 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo_url',
            field=models.URLField(default='SOME STRING'),
        ),
    ]
