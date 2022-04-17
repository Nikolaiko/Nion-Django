from django.db import models

class GameCharacter(models.Model):
    characterName = models.CharField(max_length=20)
    damage = models.IntegerField()
    health = models.IntegerField()
    avatar = models.ImageField(blank=True)
    bio = models.CharField(max_length=70)


