from django.db import models

# Create your models here.

class Payment():
    yser_name = models.CharField(max_length= 255)
    ammount_money = models.CharField(max_length= 255)
    comment= models.CharField(max_length= 255, blank= True, null=True)