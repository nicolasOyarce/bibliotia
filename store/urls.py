from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('store/', views.all_products, name='all_products'),
    path('store/<slug:category_slug>/', views.all_products, name='products_by_category'),
    path('store/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
]