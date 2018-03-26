from django.db import models

# Create your models here.

class Letters(models.Model):
    letter = models.CharField(max_length=1)
    currrent_color = models.CharField(max_length=6)
    default_color = models.CharField(max_length=6)
