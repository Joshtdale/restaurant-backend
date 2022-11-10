from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import MenuItem
from pprint import pprint

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

def menu_item(request):
    # data = list(MenuItem.objects.values(
        # title = MenuItem.title,
        # category = MenuItem.category.title,
        # "cuisine": self.cuisine.title,
        # "description": self.description,
        # "price": self.price
    # ))
    # print(MenuItem.title)
    menuItems = [i.json() for i in MenuItem.objects.all()]
    # for item in menuItems:
    #     print(item)
    return HttpResponse(json.dumps(menuItems), content_type='application/json')

    # return JsonResponse(data, safe=False)

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