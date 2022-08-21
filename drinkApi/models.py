from django.db import models

# Create your models here.


class Drink(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    described = models.CharField(max_length=500)

    def __str__(self):
        return self.name
