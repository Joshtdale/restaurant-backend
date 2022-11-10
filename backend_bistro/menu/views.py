from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import MenuItem, Category, Cuisine
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

def menu_item_cuisine(request, title):
    # data = list(MenuItem.objects.filter(cuisine_id=cuisine).values())
    data = []
    items = list(list(MenuItem.objects.filter(Cuisine.objects.get(id = item.cuisine_id)==title).values()))
    for item in items:
        cat = Category.objects.get(id = item.category_id)
        print(cat)
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
            'Spicy_level': item.spicy
        })

    return JsonResponse(data, safe=False)



def menu_item(request):
    data = []
    items = list(MenuItem.objects.all())
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
            'Spicy_level': item.spicy
        })

    return JsonResponse(data, safe=False)
    # data = list(MenuItem.objects.values(
        # title = MenuItem.title,
        # category = MenuItem.category.title,
        # "cuisine": self.cuisine.title,
        # "description": self.description,
        # "price": self.price
    # ))
    # print(MenuItem.title)
    # menuItems = [i.json() for i in MenuItem.objects.all()]
    # for item in menuItems:
    #     print(item)
    # return HttpResponse(json.dumps(menuItems), content_type='application/json')


# def books_by_year(request, year):
#     books = list(Book.objects.filter(published_year=year).values())
#     print(books)
#     if len(books) > 0:
#         return JsonResponse({'data': books})
#     else:
#         return HttpResponse('Nope')

    # return HttpResponse('You be at the year index.')

# def books_by_title(request, letter):
#     # print(letter)
#     return HttpResponse(f'letter is {letter}')