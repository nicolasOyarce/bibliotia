from django.urls import path
from .views import *


urlpatterns = [
    path('', inicio, name='inicio'),
    path('inicio/', inicio, name='inicio'),
    path('catalogo/', catalogo, name='catalogo'),
    path('checkout/', checkout, name='checkout'),
    path('item/', item, name='item'),
]


