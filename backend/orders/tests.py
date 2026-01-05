from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Order

class OrdersAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_and_list_orders(self):
        url = reverse('order-list-create')
        data = {'name': 'Test Order', 'amount': 3}
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        # list
        resp = self.client.get(url, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue(any(o['name'] == 'Test Order' for o in resp.json()))
