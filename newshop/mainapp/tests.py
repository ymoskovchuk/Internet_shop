from decimal import Decimal
from unittest import mock
from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import *
from .views import recalc_cart, AddToCartView, BaseView

from django.contrib.messages.storage.fallback import FallbackStorage


User = get_user_model()


class ShopTestCases(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(username='testuser', password='password')
        self.category = Category.objects.create(name='Ноутбуки', slug='laptops')
        image = SimpleUploadedFile('laptop_image.jpg', content=b'', content_type='image/jpg')
        self.laptop = Laptop.objects.create(
            category=self.category,
            title='Test Laptop',
            slug='test-slug',
            image=image,
            price=Decimal('10000.00'),
            diagonal='16',
            display_type='IPS',
            processor_freq='4 GHz',
            ram='8 GB',
            gpu='GeForce GTX 2060',
            time_without_charge='10 hours'
        )
        self.customer = Customer.objects.create(user=self.user, phone='111111', address='Address')
        self.cart = Cart.objects.create(owner=self.customer)
        self.cart_product = CartProduct.objects.create(
            user=self.customer,
            cart=self.cart,
            content_object=self.laptop
        )

    def test_add_to_cart(self):
        self.cart.products.add(self.cart_product)
        recalc_cart(self.cart)
        self.assertIn(self.cart_product, self.cart.products.all())
        self.assertEqual(self.cart.products.count(), 1)
        self.assertEqual(self.cart.final_price, Decimal('10000.00'))

    def test_response_from_add_to_cart_view(self):
        factory = RequestFactory()
        request = factory.get('')
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        request.user = self.user
        response = AddToCartView.as_view()(request, ct_model='laptop', slug='test-slug')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/cart/')

    def test_mock_homepage(self):
        mock_data = mock.Mock(status_code=444)
        with mock.patch('mainapp.views.BaseView.get', return_value=mock_data) as mock_data_:
            factory = RequestFactory()
            request = factory.get('')
            request.user = self.user
            response = BaseView.as_view()(request)
            self.assertEqual(response.status_code, 444)
