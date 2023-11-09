from django.contrib import admin
from django.urls import path
from books import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('products/', views.products, name='products'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('products/register/', views.register_book, name='register_book'),
    path('item/<str:id>/', views.item, name='item'),
    path('update/<str:id>/', views.update, name='update'),
    path('about/', views.about, name='about'),
    path('mod_book/', views.mod_book, name='mod_book'),
    path('delete/<str:id>/', views.delete, name='delete'),
    path('shoppingCart/', views.shoppingCart, name='shoppingCart')
]
