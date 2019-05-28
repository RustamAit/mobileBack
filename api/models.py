from django.db import models


# Create your models here.
class Person(models.Model):
    phoneNumber = models.CharField(max_length=12)
    fCMToken = models.CharField(max_length=40)


class GameData(models.Model):
    location = models.CharField(max_length=200)
    totalNumberOfPlayers = models.IntegerField
    spyNumber = models.IntegerField


class GameSession(models.Model):
    location = models.CharField(max_length=200, default="stadium")
    totalNumberOfPlayers = models.IntegerField(default=4)
    spyNumber = models.IntegerField(default=3)
    players = models.ManyToManyField(Person)
    currentPlayerNumber = models.IntegerField(default=1)
    readyPlayerNumber = models.IntegerField(default=1)
    finishedPlayerNumber = models.IntegerField(default=0)
