from django.db import models
from datetime import date

class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Cuisine(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class MenuItem(models.Model):
    title = models.CharField(max_length=300)
    # published_year = models.IntegerField(null=True, blank=True)
    # category = models.CharField(default='Lunch', max_length=30)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, default=None)
    cuisine = models.ForeignKey('Cuisine', on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(default='Its probably edible', max_length=300)
    price = models.FloatField(null=True, blank=True)
    # author = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    # def json(self):
    #     newCategory = {
    #         'title': self.category.title
    #     }
    #     # print(self.cuisine.title)
    #     return {
    #     'title': self.title,
    #     # 'category': self.category.title,
    #     'category': newCategory,
    #     "cuisine": self.cuisine.title,
    #     "description": self.description,
    #     "price": self.price
        
    #     }

    

