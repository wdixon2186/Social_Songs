# Generated by Django 2.2.7 on 2019-11-07 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_songs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
