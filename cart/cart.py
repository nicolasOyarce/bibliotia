from decimal import Decimal
from store.models import Product

class Cart:
    """
    This class manages the shopping cart
    """
    def __init__(self, request):

        self.session = request.session
        cart = self.session.get('skey')
        if 'skey' not in request.session:
            cart = self.session['skey'] = {}
        self.cart = cart

    def add(self, product, qty):
        """
        Add a product to the cart or update its quantity
        """
        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id]['qty'] = qty
        else:
            self.cart[product_id] = {'price': str(product.price), 'qty': qty}

        self.save()

    def __iter__(self):
        """
        Get the product objects and add them to the cart
        """
        product_ids = self.cart.keys()
        products = Product.products.filter(id__in=product_ids)

        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item
    
    def __len__(self):
        """
        Get the cart data and count the qty of items
        """
        return sum(item['qty'] for item in self.cart.values())
    
    def delete(self, product):
        """
        Delete item from the cart
        """
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]
        self.save()
    
    def update(self, product, qty):
        """
        Update the cart qty
        """
        product_id = str(product)

        if product_id in self.cart:
            self.cart[product_id]['qty'] = qty
        self.save()

    def get_total_price(self):
        """
        Get the cart data and calculate the total price
        """
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())
    
    def save(self):
        """
        Update the session cart
        """
        self.session.modified = True