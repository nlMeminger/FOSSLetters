from django.db import models

class Letters(models.Model):
    letter = models.CharField(max_length=1)
    currrent_color = models.CharField(max_length=6)
    default_color = models.CharField(max_length=6)
