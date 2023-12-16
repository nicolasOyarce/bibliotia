from django.db import models

from accounts.models import Account
from store.models import Product, Variation


class Cart(models.Model):
    cart_id    = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'cart'
        verbose_name_plural = 'carts'
        
    def __str__(self):
        return self.cart_id
    
class CartItem(models.Model):
    user       = models.ForeignKey(Account, null=True, blank=True, on_delete=models.CASCADE)
    product    = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation, blank=True)
    cart       = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    quantity   = models.IntegerField()
    is_active  = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'cart item'
        verbose_name_plural = 'cart items'
        
    def sub_total(self):
        """
        This method will return the total price of the product
        """
        return self.product.price * self.quantity
    
    def __str__(self):
        return str(self.product)