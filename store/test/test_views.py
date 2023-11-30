from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse
from django.utils.module_loading import import_module

from store.models import Category, Product
from store.views import products_all


class TestViewsResponses(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create(username='admin')
        self.category = Category.objects.create(name='django', slug='django')
        self.product = Product.objects.create(category=self.category, title='django beginners', created_by=self.user, slug='django-beginners', price='20.00', image='django')

    def tearDown(self):
        self.user.delete()
        self.category.delete()
        self.product.delete()

    def test_url_allowed_hosts(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        response = self.client.get(reverse('store:product_detail', args=['django-beginners']))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        response = self.client.get(reverse('store:category_list', args=['django']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        request = HttpRequest()
        engine = import_module(settings.SESSION_ENGINE)
        request.session = engine.SessionStore()
        response = products_all(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Inicio</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
