from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import get_object_or_404

# Create your views here.

# View for the categories
def categories(request):

    return {
        'categories': Category.objects.all()
    }


# View for the home page
def all_products(request):

    products = Product.objects.all()
    
    return render(request, 'store/home.html', {
        'products': products
        })


# View for the product detail page
def product_detail(request, slug):

    product = get_object_or_404(Product, slug=slug, in_stock=True)

    return render(request, 'store/detail.html', {
        'product': product
        })