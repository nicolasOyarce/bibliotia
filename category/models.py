from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    category_name = models.CharField(max_length=200, unique=True)
    slug          = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('category_name', ) 
    
    def get_url(self):
        return reverse('store:products_by_category', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    
    def __str__(self):
        return self.category_name

    