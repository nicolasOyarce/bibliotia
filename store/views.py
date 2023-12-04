from django.shortcuts import render
from .models import Product
from category.models import Category
from django.shortcuts import get_object_or_404

def home(request):
    """
    View for the home page
    """
    products = Product.objects.all().filter(is_available=True)
    return render(request, 'store/home.html', {
        'products': products
    })

def all_products(request, category_slug=None):
    """
    View for the all products page
    """
    if category_slug:
        category =  get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)
        products_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        products_count = products.count()

    return render(request, 'store/all_products.html', {
        'products': products,
        'products_count': products_count,
    })

def product_detail(request, category_slug, product_slug):
    """
    View for the product detail page
    """
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'store/product_detail.html', {
        'single_product': single_product
    })