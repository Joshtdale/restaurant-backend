from django.db import models
from datetime import date
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator

class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Cuisine(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Ingredients(models.Model):
    name = models.CharField(null=True, blank=True, max_length=30)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(default='Lexington',null=True, blank=True, max_length=30)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    title = models.CharField(max_length=300)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, default=None)
    cuisine = models.ForeignKey('Cuisine', on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(default='Its probably edible', max_length=300)
    price = models.FloatField(null=True, blank=True)
    spicy = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    ingredients = models.ManyToManyField(Ingredients)
    restaurant = models.ManyToManyField(Restaurant)

    def __str__(self):
        return self.title

    

