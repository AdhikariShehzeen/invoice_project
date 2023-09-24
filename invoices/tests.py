from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer

class InvoicesTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice_data = {
            'customer_name': 'Test Customer'
        }
        self.invoice = Invoice.objects.create(**self.invoice_data)
        self.invoice_detail_data = {
            'invoice': self.invoice,
            'description': 'Test Description',
            'quantity': 1,
            'unit_price': '10.00',
            'price': '10.00'
        }
        self.invoice_detail = InvoiceDetail.objects.create(**self.invoice_detail_data)

    def test_create_invoice(self):
        data = {'customer_name': 'New Test Customer'}
        response = self.client.post(reverse('invoice'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 2)

    def test_get_invoice(self):
        response = self.client.get(reverse('invoice'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_specific_invoice(self):
        response = self.client.get(reverse('invoice', args=[self.invoice.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['customer_name'], 'Test Customer')

    def test_update_invoice(self):
        data = {'customer_name': 'Updated Test Customer'}
        response = self.client.put(reverse('invoice', args=[self.invoice.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.invoice.refresh_from_db()
        self.assertEqual(self.invoice.customer_name, 'Updated Test Customer')

    def test_delete_invoice(self):
        response = self.client.delete(reverse('invoice', args=[self.invoice.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Invoice.objects.count(), 0)

class InvoiceDetailsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice_data = {
            'customer_name': 'Test Customer'
        }
        self.invoice = Invoice.objects.create(**self.invoice_data)
        self.invoice_detail_data = {
            'invoice': self.invoice,
            'description': 'Test Description',
            'quantity': 1,
            'unit_price': '10.00',
            'price': '10.00'
        }
        self.invoice_detail = InvoiceDetail.objects.create(**self.invoice_detail_data)

    def test_create_invoice_detail(self):
        data = {
            'customer_name': 'New Test Customer',
            'description': 'New Test Description',
            'quantity': 2,
            'unit_price': '20.00',
            'price': '40.00',
            'invoice': self.invoice.id
        }
        response = self.client.post(reverse('invoice-details'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(InvoiceDetail.objects.count(), 2)

    def test_get_invoice_details(self):
        response = self.client.get(reverse('invoice-details'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_specific_invoice_detail(self):
        response = self.client.get(reverse('invoice-details', args=[self.invoice_detail.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], 'Test Description')

    def test_update_invoice_detail(self):
        data = {
            'customer_name': 'Updated Test Customer',
            'description': 'Updated Test Description',
            'quantity': 1,
            'unit_price': '20.00',
            'price': '40.00',
            'invoice': self.invoice.id
        }
                
        response = self.client.put(reverse('invoice-details', args=[self.invoice_detail.id]), data, format='json')
        print(response.data)  
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.invoice_detail.refresh_from_db()
        self.assertEqual(self.invoice_detail.description, 'Updated Test Description')

    def test_delete_invoice_detail(self):
        response = self.client.delete(reverse('invoice-details', args=[self.invoice_detail.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(InvoiceDetail.objects.count(), 0)
