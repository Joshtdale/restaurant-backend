from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json, csv
from .models import MenuItem, Category, Cuisine, Ingredients
from pprint import pprint
from django.forms.models import model_to_dict

def some_view(request):
    data = list(SomeModel.objects.values())
    return JsonResponse(data, safe=False)

# def get_books(request):
#     books = list(Book.objects.values())
#     print(books)
#     return JsonResponse({'data': books})
    # if request.method == 'GET':
    #     print('GET request')
    # # pprint(dir(request))
    # else:
    #     print('NOT A GET request')

    # return HttpResponse('Books be workin\'')

def menu_item_title(request):
    data = list(MenuItem.objects.values(
        'title'
    ))
    return JsonResponse(data, safe=False)

def menu_item_cuisine_id(request, title):
    data = []
    items = list(MenuItem.objects.filter(cuisine__id=title).all())
    # items = list(MenuItem.objects.all())
    # print(title)
    for item in items:
        cat = Category.objects.get(id = item.category_id)
        # print(cat)
        cui = Cuisine.objects.get(id = item.cuisine_id)
        # ing = Ingredients.objects.get(id = item.ingredients_id)
        data.append({
            'title': item.title,
            'category': {
                'title': cat.title,
                'uppercase_title': cat.title.upper()
            },
            "cuisine": model_to_dict(cui, exclude=['id']),
            # 'ingredients': model_to_dict(ing),
            "description": item.description,
            "price": item.price,
            'Spicy_level': item.spicy
        })
    return JsonResponse(data, safe=False)


def menu_item_category(request, title):
    # cat = Category.objects.get(id = MenuItem__category_id)
    # data = list(MenuItem.objects.filter(cuisine__id=title).values())
    # print('working', title)
    # print('working', cat)
    data = []
    items = list(MenuItem.objects.filter(category__title = title))
    # print(title)
    for item in items:
        cat = Category.objects.get(id = item.category_id)
    #     # print(cat)
        cui = Cuisine.objects.get(id = item.cuisine_id)
        print(item.category)
        # if item.category == title:
        data.append({
            'title': item.title,
            'category': {
                'title': cat.title,
                'uppercase_title': cat.title.upper()
            },
            "cuisine": model_to_dict(cui, exclude=['id']),
            "description": item.description,
            "price": item.price,
            'Spicy_level': item.spicy
        })


    return JsonResponse(data, safe=False)



def menu_item(request):
    data = []
    items = list(MenuItem.objects.all())
    # ingredient = list(Ingredients.objects.all())
    # ing = Ingredients.objects.get(id = ingredients.ingredients_id)
    for item in items:
        cat = Category.objects.get(id = item.category_id)
        cui = Cuisine.objects.get(id = item.cuisine_id)

        data.append({
            'title': item.title,
            'category': {
                'title': cat.title,
                'uppercase_title': cat.title.upper()
            },
            "cuisine": model_to_dict(cui, exclude=['id']),
            "description": item.description,
            "price": item.price,
            'Spicy_level': item.spicy,
            'ingredients': {
                'name': list(item.ingredients.values())
            },
            'location': {
                'name': list(item.restaurant.values())
                }
            # for i in ingredient:
            #     'name': i.name
            # }

                # data.append({
            
                # })
            # 'ingredients': model_to_dict(ing)

        })

    return JsonResponse(data, safe=False)

def menu_cvs(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="Menu.csv"'},
    )

    items = MenuItem.objects.all()
    writer = csv.writer(response)
    writer.writerow(['Name', 'Descriptions', 'Price'])
    for item in items:
        writer.writerow([item.title, item.description, item.price])

    return response