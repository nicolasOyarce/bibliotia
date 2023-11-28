from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from store.models import Product
from .cart import Cart

# Cart summary view
def cart_summary(request):
    cart = Cart(request)
    return render(request, 'cart/summary.html',{
        'cart': cart
    })

# Add to cart view
def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, qty=product_qty)

        cartqty = cart.__len__()
        response = JsonResponse({'qty': cartqty})

        return response
    