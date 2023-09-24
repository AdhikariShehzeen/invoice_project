from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Invoices, InvoiceDetails


urlpatterns = [
    # path('', include(router.urls)),
    path('invoice/', Invoices, name = 'invoice'),
    path('invoice-details/', InvoiceDetails, name = 'invoice-details'),
    path('invoice/<int:invoice_id>/', Invoices, name = 'invoice'),
    path('invoice-details/<int:d_id>/', InvoiceDetails, name = 'invoice-details'),
    
]



