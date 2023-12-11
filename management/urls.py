from django.urls import path

from . import views

app_name = 'management'

urlpatterns = [
    #Products
    path('products/', views.management_product, name='management_products'),
    path('product/add/', views.product_add, name='product_add'),
    path('product/edit/<int:id>/', views.product_edit, name='product_edit'),
    path('product/delete/<int:id>/', views.product_delete, name='product_delete'),

    #Orders
    path('orders/', views.management_order, name='management_orders'),

    #Users
    path('users/', views.management_users, name='management_users'),
    path('user/delete/<int:id>/', views.user_delete, name='user_delete'),

    #Categories
    path('categories/', views.management_categories, name='management_categories'),
    path('category/add/', views.category_add, name='category_add'),
    path('category/edit/<int:id>/', views.category_edit, name='category_edit'),
    path('category/delete/<int:id>/', views.category_delete, name='category_delete'),
]