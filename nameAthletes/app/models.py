from django.db import models


class Athlete(models.Model):
    name = models.CharField(max_length=100)
    sport = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return f'{self.name} - {self.sport}'

class Game(models.Model):
    length = models.IntegerField()
    id = models.AutoField(primary_key=True)
    athletes = models.ManyToManyField(Athlete)
    start_time = models.DateTimeField()
    def __str__(self):
        return f'game - {self.id}'