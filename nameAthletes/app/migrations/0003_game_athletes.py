# Generated by Django 5.1.4 on 2025-01-06 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='athletes',
            field=models.ManyToManyField(to='app.athlete'),
        ),
    ]
