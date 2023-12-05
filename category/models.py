from django.db import models
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(max_length=200, unique=True)
    slug          = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('category_name', ) 
    
    def get_url(self):
        return reverse('store:products_by_category', args=[self.slug])
    
    def __str__(self):
        return self.category_name

    