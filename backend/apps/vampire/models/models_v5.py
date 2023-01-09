from django.db import models

from apps.core.models import Character, CharacterComponent

from .common import VampireClan

class VampireCC(CharacterComponent):
    clan = models.ForeignKey(VampireClan, on_delete=models.CASCADE)
    sire = models.ForeignKey(Character, on_delete=models.SET_NULL, null=True, blank=True, default=None, related_name='vampire_sire')

    title = models.CharField(max_length=50, null=True, blank=True)

    embrace_date = models.DateTimeField(null=True, blank=True)

class HumanCC(CharacterComponent):
    birth_date = models.DateTimeField()


class V5CharacterStats(CharacterComponent):
    # Atributes

    ## Physical
    strength = models.SmallIntegerField(default=1)
    dexterity = models.SmallIntegerField(default=1)
    stamina = models.SmallIntegerField(default=1)

    ## Social
    charisma = models.SmallIntegerField(default=1)
    manipulation = models.SmallIntegerField(default=1)
    composure = models.SmallIntegerField(default=1)
    
    ## Mental
    intelligence = models.SmallIntegerField(default=1)
    wits = models.SmallIntegerField(default=1)
    resolve = models.SmallIntegerField(default=1)


    # Habilities
    athletics = models.SmallIntegerField(default=0)
    brawl = models.SmallIntegerField(default=0)
    craft = models.SmallIntegerField(default=0)
    drive = models.SmallIntegerField(default=0)
    firearms = models.SmallIntegerField(default=0)
    larceny = models.SmallIntegerField(default=0)
    melee = models.SmallIntegerField(default=0)
    stealth = models.SmallIntegerField(default=0)
    survival = models.SmallIntegerField(default=0)

    animal_ken = models.SmallIntegerField(default=0)
    etiquette = models.SmallIntegerField(default=0)
    insight = models.SmallIntegerField(default=0)
    intimidation = models.SmallIntegerField(default=0)
    leadership = models.SmallIntegerField(default=0)
    performance = models.SmallIntegerField(default=0)
    persuasion = models.SmallIntegerField(default=0)
    streetwise = models.SmallIntegerField(default=0)
    subterfuge = models.SmallIntegerField(default=0)

    academics = models.SmallIntegerField(default=0)
    awareness = models.SmallIntegerField(default=0)
    finance = models.SmallIntegerField(default=0)
    investigation = models.SmallIntegerField(default=0)
    medicine = models.SmallIntegerField(default=0)
    occult = models.SmallIntegerField(default=0)
    politics = models.SmallIntegerField(default=0)
    science = models.SmallIntegerField(default=0)
    technology = models.SmallIntegerField(default=0)


    ## General
    health = models.SmallIntegerField(default=0)
    humanity = models.SmallIntegerField(default=0)
    willpowet = models.SmallIntegerField(default=0)

    ansia = models.SmallIntegerField(default=0)
    blood_potence = models.SmallIntegerField(default=0)
    

class Discipline(models.Model):
    name = models.CharField(max_length=25)

class DisciplineDot(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)

    name = models.CharField(max_length=25)
    description = models.TextField()

class VampireDiscipline(CharacterComponent):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)

    dots = models.ManyToManyField(DisciplineDot)


class Merit(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()

class MeritDots(models.Model):
    merit = models.ForeignKey(Merit, on_delete=models.CASCADE)
    description = models.TextField()
    cost = models.SmallIntegerField(default=1)

class CharacterMerits(CharacterComponent):
    merit = models.ForeignKey(MeritDots, on_delete=models.CASCADE)
