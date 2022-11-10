from django.contrib import admin
from .models import MenuItem, Category, Cuisine

# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    fields = ('title', 'category', 'description', 'price', 'cuisine')

admin.site.register(MenuItem, MenuAdmin)
admin.site.register(Category)
admin.site.register(Cuisine)