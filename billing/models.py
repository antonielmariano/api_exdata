from django.db import models


class Billing(models.Model):
    client_code = models.IntegerField()
    category_product = models.CharField(max_length=256)
    sku_product = models.CharField(max_length=256)
    date = models.DateField()
    quantity = models.IntegerField()
    value_billing = models.DecimalField(decimal_places=2, max_digits=15)

    def __repr__(self) -> str:
        return f'{self.id} - {self.client_code}'
    
