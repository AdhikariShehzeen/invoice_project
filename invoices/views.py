from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Invoices(request, invoice_id=None):
    if request.method == 'GET':
        if invoice_id:
            try:
                invoice1 = Invoice.objects.get(id=invoice_id)
                serializer = InvoiceSerializer(invoice1)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Invoice.DoesNotExist:
                return Response({"detail": "Invoice not found"}, status=status.HTTP_404_NOT_FOUND)

        all_invoice = Invoice.objects.all()
        serializer = InvoiceSerializer(all_invoice, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    
    if request.method  == 'POST':
        '''
        Create a post request to create invoice for a customer
        '''

        data = {
            'customer_name' : request.data.get('customer_name'),
            # 'invoice': request.data.get('invoice')
            
        }

        serializer = InvoiceSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        '''
        Updates the invoice with given invoice id if exists
        '''
        invoice_instance = Invoice.objects.get(id=invoice_id)
        if not invoice_instance:
            return Response(
                {"res": "Object does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'customer_name' : request.data.get('customer_name'),
            
        }
        serializer = InvoiceSerializer(instance = invoice_instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        '''
        Delete the invoice with given invoice id if exists
        '''
        invoice_instance = Invoice.objects.get(id=invoice_id)
        if not invoice_instance:
            return Response({"res": "Object does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        invoice_instance.delete()
        return Response( {"res": "Object deleted!"},status=status.HTTP_200_OK)



    
            
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def InvoiceDetails(request, d_id=None):

    if request.method == 'GET':
        if d_id:
            try:
                detail_instance = InvoiceDetail.objects.get(id=d_id)
                serializer = InvoiceDetailSerializer(detail_instance)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except InvoiceDetail.DoesNotExist:
                return Response({"detail": "Invoice  detail not found"}, status=status.HTTP_404_NOT_FOUND)
            
        invoice_details = InvoiceDetail.objects.all()
        serializer = InvoiceDetailSerializer(invoice_details, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    

    if request.method  == 'POST':
        '''
        Create a post request to create invoice for a customer
        '''

        data = {
            'customer_name' : request.data.get('customer_name'),
            'description': request.data.get('description'),
            'quantity' : request.data.get('quantity'),
            'unit_price' : request.data.get('unit_price'),
            'price' : request.data.get('price'),
            'invoice': request.data.get('invoice')
            
        }

        serializer = InvoiceDetailSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    if request.method == 'PUT':
        '''
        Updates the invoice detail with given detail id if exists
        '''
        detail_instance = InvoiceDetail.objects.get(id=d_id)
        if not detail_instance:
            return Response(
                {"res": "Object does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'customer_name' : request.data.get('customer_name'),
            'description': request.data.get('description'),
            'quantity' : request.data.get('quantity'),
            'unit_price' : request.data.get('unit_price'),
            'price' : request.data.get('price'),
            'invoice': request.data.get('invoice')
            
        }
        serializer = InvoiceDetailSerializer(instance = detail_instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        '''
        Delete the invoice with given invoice id if exists
        '''
        detail_instance = InvoiceDetail.objects.get(id=d_id)
        if not detail_instance:
            return Response({"res": "Object does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        detail_instance.delete()
        return Response( {"res": "Object deleted!"},status=status.HTTP_200_OK)


    

    





