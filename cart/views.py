from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from store.models import Product

from .cart import Cart


# Cart summary view
def cart_summary(request):
    """
    A view that renders the cart contents page
    """
    cart = Cart(request)
    return render(request, 'cart/summary.html',{
        'cart': cart
    })

def cart_add(request):
    """
    Add a product to the cart
    """
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, qty=product_qty)

        cartqty = cart.__len__()
        response = JsonResponse({'qty': cartqty})

        return response
    
def cart_delete(request):
    """
    Delete a product from the cart
    """
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        cart.delete(product=product_id)

        cartqty = cart.__len__()
        carttotal = cart.get_total_price()
        response = JsonResponse({'qty': cartqty, 'subtotal': carttotal})

        return response

def cart_update(request):
    """
    Update the cart qty
    """
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        cart.update(product=product_id, qty=product_qty)

        cartqty = cart.__len__()
        carttotal = cart.get_total_price()
        response = JsonResponse({'qty': cartqty, 'subtotal': carttotal})

        return response