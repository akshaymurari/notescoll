from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=30)
    nofp = models.IntegerField()
    prize = models.DecimalField(max_digits=10,decimal_places=2)