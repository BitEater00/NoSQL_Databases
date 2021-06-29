from django.db import models

# Create your models here.


class AllCategories(models.Model):
    image = models.CharField(max_length=5000)
    categoryname = models.CharField(max_length=35)
    categorycount = models.IntegerField()
