from django.test import TestCase
from store.models import Category, Product

# Test Category Model
class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')
    
    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry(self):
        """
        Test Category model default name
        """
        data = self.data1
        self.assertEqual(str(data), 'django')


# Test Product Model
class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name='django', slug='django')
        self.data1 = Product.objects.create(category_id=1, title='django beginners', created_by_id=1, slug='django-beginners', price='20.00', image='django')
    
    def test_products_model_entry(self):
        """
        Test Product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
    
    def test_products_model_entry(self):
        """
        Test Product model default name
        """
        data = self.data1
        self.assertEqual(str(data), 'django beginners')