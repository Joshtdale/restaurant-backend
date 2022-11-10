from django.urls import path

from . import views

urlpatterns = [
    # path('books/', views.get_books),
    # path('books/<int:year>', views.books_by_year),
    # path('books/<str:letter>', views.books_by_title),
    path('menuitems/', views.menu_item),
    # path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]