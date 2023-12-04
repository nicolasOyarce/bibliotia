from django.db import models
from django.urls import reverse
from category.models import Category


class Product(models.Model):
    title        = models.CharField(max_length=255)
    author       = models.CharField(max_length=255)
    editorial    = models.CharField(max_length=255)
    slug         = models.SlugField(unique=True)
    description  = models.TextField()
    price        = models.IntegerField()
    stock        = models.IntegerField()
    image        = models.ImageField(upload_to='products')
    is_available = models.BooleanField(default=True)
    category     = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at   = models.DateTimeField(auto_now_add=True)
    modified_at  = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ('title', )

    def get_url(self):
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return self.title