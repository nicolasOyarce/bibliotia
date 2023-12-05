from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from cart.models import CartItem
from cart.views import _cart_id
from category.models import Category

from .models import Product


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
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        products_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        products_count = products.count()

    return render(request, 'store/all_products.html', {
        'products': paged_products,
        'products_count': products_count,
    })

def product_detail(request, slug):
    """
    View for the product detail page
    """
    try:
        single_product = Product.objects.get(slug=slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e
    return render(request, 'store/product_detail.html', {
        'single_product': single_product,
        'in_cart': in_cart,
    })