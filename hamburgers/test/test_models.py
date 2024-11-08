from hamburgers.models import Hamburger
from django.test import TestCase

class HamburgerTestCase(TestCase):

    def setUp(self):
        Hamburger.objects.create(name='hamburger', price = 150.00)


    def test_hamburger_creation(self):
        product = Hamburger.objects.create(name='hamburger')
        self.assertEqual(product.price, 150.00)

    def test_hamburger_str_method(self):
        product = Hamburger.objects.get(name = 'hamburger')
        self.assertEqual(str(product), 'hamburger')