# Generated by Django 5.1.4 on 2025-01-05 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('sport', models.CharField(max_length=100)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
