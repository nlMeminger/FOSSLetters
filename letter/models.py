from django.db import models

# Create your models here.

class Letter(models.Model):
    letter = models.CharField(max_length=1)

    cur_r = models.CharField(max_length=3, default='255')
    cur_g = models.CharField(max_length=3, default='255')
    cur_b = models.CharField(max_length=3, default='255')

    def_r = models.CharField(max_length=3, default='255')
    def_g = models.CharField(max_length=3, default='255')
    def_b = models.CharField(max_length=3, default='255')

    def __unicode__(self):
       return self.letter
