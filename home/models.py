from django.db import models

# Create your models here.

class items(models.Model):
    uid = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    avalability = models.IntegerField()
    des = models.CharField(max_length=1000)
    rating = models.IntegerField()

    def __str__(self):
        return self.uid

class Cart(models.Model):
    uid = models.CharField(max_length=10)
    username = models.CharField(max_length=50)
