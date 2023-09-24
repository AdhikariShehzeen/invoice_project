from django.db import models


class Invoice(models.Model):
    date = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    customer_name = models.CharField(max_length=255)

    def __str__(self):
        return f"Invoice #{self.id} - {self.customer_name}"

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='invoice_details', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detail #{self.id} - {self.description}"
