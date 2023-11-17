from django.contrib import admin
from django.urls import path, include
from books import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('products/', views.products, name='products'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('products/register/', views.register_book, name='register_book'),
    path('item/<int:id>/', views.item, name='item'),
    path('update/<int:id>/', views.update, name='update'),
    path('about/', views.about, name='about'),
    path('mod_book/', views.mod_book, name='mod_book'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('shoppingCart/', views.shoppingCart, name='shoppingCart'),
    path('contact/', views.contact, name="contact")
]
