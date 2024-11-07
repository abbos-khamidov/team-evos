from django.test import TestCase
from app.models import Product

class ProductModelTest(TestCase):
    
    def setUp(self):
        Product.objects.create(name="Laptop", price=1000.00)

    def test_product_creation(self):
        product = Product.objects.get(name="Laptop")
        self.assertEqual(product.price, 1000.00)

    def test_product_str_method(self):
        product = Product.objects.get(name="Laptop")
        self.assertEqual(str(product), "Laptop")