from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, redirect, render

from store.models import Product

from .models import Cart, CartItem


def _cart_id(request):
    """
    This function will return the session ID of the current session
    """
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def cart_add(request, product_id):
    """
    This view function will add the product to the cart
    """
    product = Product.objects.get(id=product_id) 
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request)) 
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
                cart_id = _cart_id(request)
            )
        cart.save()
    
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart) 
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
                product = product,
                quantity = 1,
                cart = cart
            )
        cart_item.save()

    return redirect('cart:cart')

def cart_decrement(request, product_id):
    """
    This view function will decrement the product from the cart
    """
    cart = Cart.objects.get(cart_id=_cart_id(request)) 
    product = get_object_or_404(Product, id=product_id) 
    cart_item = CartItem.objects.get(product=product, cart=cart) 
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    
    return redirect('cart:cart')

def cart_remove(request, product_id):
    """
    This view function will remove the product from the cart
    """
    cart = Cart.objects.get(cart_id=_cart_id(request)) 
    product = get_object_or_404(Product, id=product_id) 
    cart_item = CartItem.objects.get(product=product, cart=cart) 
    cart_item.delete()
    
    return redirect('cart:cart')

def cart(request, total=0, quantity=0, cart_items=None):
    """
    This view function will render the cart page
    """
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True) 
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity) 
            quantity += cart_item.quantity
        send = 4500
        grand_total = total + send
    except ObjectDoesNotExist:
        pass


    return render(request, 'cart/summary.html',{
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'send': send,
        'grand_total': grand_total,
    })