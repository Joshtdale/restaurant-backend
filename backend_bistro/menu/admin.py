from django.contrib import admin
from .models import MenuItem, Category, Cuisine, Ingredients, Restaurant

# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    fields = ('title', 'category', 'description', 'price', 'cuisine', 'spicy', 'ingredients', 'restaurant')

admin.site.register(MenuItem, MenuAdmin)
admin.site.register(Category)
admin.site.register(Cuisine)
admin.site.register(Ingredients)
admin.site.register(Restaurant)