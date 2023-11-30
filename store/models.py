from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.

# Model for the product manager
class ProductManager(models.Manager):

    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(in_stock=True)
    
# Model for the category
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('name', ) 

    def __str__(self):
        return self.name
    
# Model for the product
class Product(models.Model):
    category    = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    created_by  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='product_creator')
    title       = models.CharField(max_length=200, db_index=True) 
    author      = models.CharField(max_length=200, db_index=True)
    editorial   = models.CharField(max_length=200, db_index=True)
    slug        = models.SlugField(max_length=200, db_index=True)
    image       = models.ImageField(upload_to='products/', default='products/default.png') 
    description = models.TextField(blank=True) 
    price       = models.DecimalField(max_digits=10, decimal_places=2) 
    in_stock    = models.BooleanField(default=True)
    is_active   = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    objects     = models.Manager()
    products    = ProductManager()

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ('-created', ) 

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])
    
    def __str__(self):
        return self.title