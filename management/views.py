from django.shortcuts import render
from store.models import Product
from accounts.models import Account

def management_product(request):
    products = Product.objects.all()
    return render(request, 'management/products.html', {
        'products': products,
    })

def management_order(request):
    return render(request, 'management/orders.html', {})

def management_users(request):
    users = Account.objects.all()
    return render(request, 'management/users.html', {
        'users': users,
    })

def management_categories(request):
    return render(request, 'management/categories.html', {})