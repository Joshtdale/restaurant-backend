from django.urls import path

from . import views

urlpatterns = [

    path('menuitems/', views.menu_item),
    path('menuitems/name', views.menu_item_title),
    path('menuitems/cuisine/<str:title>', views.menu_item_cuisine),
]