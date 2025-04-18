from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Ad, ExchangeProposal

class AdModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='pass')
        self.ad = Ad.objects.create(user=self.user, title='Test Ad', description='Desc', category='Cat', condition='new')

    def test_ad_str(self):
        self.assertEqual(str(self.ad), 'Test Ad (tester)')

class AdAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='apiuser', password='pass')
        self.client.login(username='apiuser', password='pass')

    def test_create_ad(self):
        data = {
            'title': 'API Ad',
            'description': 'API Desc',
            'category': 'Cat',
            'condition': 'new'
        }
        response = self.client.post('/api/ads/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['title'], 'API Ad')