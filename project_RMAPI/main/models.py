from django.db import models
from django.utils import timezone
# Create your models here.

class Location(models.Model):
    locationType = [
        ("planet", "PLANET"),
        ("cluster", "CLUSTER"),
        ("space_station", "SPACE STATION"),
        ("microverse", "MICROVERSE"),
        ("tv", "TV"),
        ("resort", "RESORT"),
        ("fantasy_town", "FANTASY TOWN"),
        ("dream", "DREAM")
    ]
    name = models.CharField(max_length=150)
    locationType = models.CharField(max_length=100, choices=locationType, blank=True, null=True)
    dimension = models.CharField(max_length=150, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Character(models.Model):

    statusType = [
        ("alive", "ALIVE"),
        ("dead", "DEAD"),
        ("unknown", "UNKNOWN"),
    ]


    specieType = [
        ("human", "HUMAN"),
        ("alien", "ALIEN"),
    ]

    genderType = [
        ("male", "MALE"),
        ("female", "FEM"),
        ("others", "OTHERS"),
    ]

    characterType = [
        ("genetic_experiment", "GENETIC EXPERIMENT"),
        ("Superhuman (Ghost trains summoner)", "SUPERHUMAN"),
        ("parasite", "PARASITE"),
    ]

    name = models.CharField(max_length=150)
    status = models.CharField(max_length=50, choices=statusType, blank=True, null=True)
    species = models.CharField(max_length=150, choices= specieType,blank=True, null=True)
    charaterType = models.CharField(max_length=50, choices= characterType ,blank=True, null=True)
    gender = models.CharField(max_length=50, choices=genderType, blank=True, null=True)
    origin = models.ForeignKey(Location, related_name="location", blank=True, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Episode(models.Model):
    name = models.CharField(max_length=150)
    air_date = models.DateField()
    episode = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Characters_Episode():
    character_fk = models.ForeignKey(Character, related_name="location", blank=False, null=False, on_delete=models.CASCADE)
    episode_fk = models.ForeignKey(Episode, related_name="location", blank=False, null=False, on_delete=models.CASCADE)
