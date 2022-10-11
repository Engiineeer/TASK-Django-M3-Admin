from email.policy import default
from django.db import models
from django.forms import CharField

# Create your models here.


class Pokemon(models.Model):
    class PokemonType(models.TextChoices):
        WATER = 'WA'
        GRASS = 'GR'
        GHOST = 'GH'
        STEEL = 'ST'
        FAIRY = 'FA'

    name = models.CharField(max_length=30)
    type = models.CharField(
        max_length=10, choices=PokemonType.choices, default="GHOST")
    hp = models.PositiveIntegerField(default=10)
    active = models.BooleanField(default=True)
    name_fr = models.CharField(max_length=30, default="")
    name_ar = models.CharField(max_length=30, default="")
    name_jp = models.CharField(max_length=30, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
