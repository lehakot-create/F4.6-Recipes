from django.db import models
from django.contrib.postgres.fields import ArrayField

class Recipes(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    ingredients = ArrayField(models.CharField(max_length=128))


class Category(models.Model):
    name = models.CharField(max_length=32)
