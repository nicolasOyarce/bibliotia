from django.urls import path
from . import views

app_name = 'management'

urlpatterns = [
    path('products/', views.management_product, name='management_products'),
    path('orders/', views.management_order, name='management_orders'),
    path('users/', views.management_users, name='management_users'),
    path('categories/', views.management_categories, name='management_categories'),
]