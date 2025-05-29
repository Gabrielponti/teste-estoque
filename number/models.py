from django.db import models
from stocks.models import Stock


class Number(models.Model):
    name_number = models.CharField(max_length=4)

    def __str__(self):
        return self.name_number


class NumberQuantity(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='number_quantities')
    number = models.ForeignKey(Number, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)


    class Meta:
        unique_together = ('stock', 'number')  
    
    def __str__(self):
       return f"{self.stock.name} - {self.number.name_number}: {self.quantity}"
