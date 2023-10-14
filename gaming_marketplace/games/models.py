from django.db import models

# Create your models here.

class Game():
    game = models.CharField(max_length= 255)
    price = models.CharField(max_length= 255)
    creator= models.CharField(max_length= 255)
