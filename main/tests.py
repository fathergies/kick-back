from django.test import TestCase, Client
from .models import Product

class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/burhan_always_exists/')
        self.assertEqual(response.status_code, 404)

    def test_product_creation(self):
        product = Product.objects.create(
            name="Jersey",
            price=100000,
            description="Jersey resmi",
            thumbnail="http://example.com/jersey.jpg",
            category="Clothes",
            is_featured=True
        )
        self.assertEqual(product.name, "Jersey")
        self.assertTrue(product.is_featured)