from django.db import models

# Create your models here.
class PriceList(models.Model):
    species = models.CharField(max_length=128, default='')
    item = models.CharField(max_length=128, default='')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.item