from datetime import datetime
from django.db import models

from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL

class Chronicle(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()

    current_date = models.DateField()

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="chronicles_owned_set")
    players = models.ManyToManyField(User, through="ChroniclePlayers", related_name="chronicles_as_player_set")

    def __str__(self):
        return self.name


class ChroniclePlayers(models.Model):
    class Role(models.IntegerChoices):
        ST = 1, "Story teller"
        PLAYER = 2, "Player"
        GUEST = 3, "Guest"

    chronicle = models.ForeignKey(Chronicle, on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE)

    role = models.PositiveSmallIntegerField(
        choices=Role.choices,
        default=Role.ST
    )

class ChronicleData(models.Model):
    chronicle = models.ForeignKey(Chronicle, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Character(ChronicleData):
    name = models.CharField(max_length=25)

    story = models.TextField(null=True, blank=True)
    
    pc = models.BooleanField()

    relationships = models.ManyToManyField('Character', through='CharacterRelationship')

    def __str__(self):
        return self.name


class CharacterRelationship(models.Model):
    class Meta:
        unique_together = (('character1', 'character2'),)

    character1 = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='relationship_character1')
    character2 = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='relationship_character2')

    FEELING_CHOICES = [
        ('Love', (
            ('lover', 'Lover'),
            ('married', 'Married')
        )),
        ('enemy', 'Enemy'),
        ('friend', 'Friend')
    ]

    feeling = models.CharField(max_length=10, choices=FEELING_CHOICES)


class CharacterComponent(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE)

    class Meta:
        abstract = True




class Plot(ChronicleData):
    name = models.CharField(max_length=25)
    description = models.TextField()

    def __str__(self):
        return self.name


class PlotStages(models.Model):
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE)
    description = models.TextField()


class Location(ChronicleData):
    name = models.CharField(max_length=25)



class Sesion(ChronicleData):
    title = models.CharField(max_length=25)

    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

class Event(models.Model):
    sesion = models.ForeignKey(Sesion, on_delete=models.CASCADE)
    text = models.TextField()


