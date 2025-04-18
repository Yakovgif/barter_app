from django.test import TestCase
from django.contrib.auth.models import User
from .models import Ad

class AdModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_create_ad(self):
        ad = Ad.objects.create(
            user=self.user,
            title='Тестовое объявление',
            description='Описание товара',
            category='Электроника',
            condition='new'
        )
        self.assertEqual(str(ad), 'Тестовое объявление (testuser)')