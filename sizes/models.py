from django.db import models
from stocks.models import Stock

class Size(models.Model):
    size = models.CharField(max_length=10, unique=True)
   
    def __str__(self):
        return self.size


class SizeQuantity(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='size_quantities')
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ('stock', 'size')  # Evita duplicatas

    def __str__(self):
        return f"{self.stock.name} - {self.size.size}: {self.quantity}"