from django.db import models
from django.utils import timezone
import json

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    episode_number = models.IntegerField()
    main_characters = models.TextField()
    description = models.TextField()
    poster = models.CharField(max_length=200)
    hero_image = models.CharField(max_length=200)
    def character_list(self, charaters):
        self.main_characters = json.dumps(charaters)
        self.save()
    def __str__(self):
        return self.title