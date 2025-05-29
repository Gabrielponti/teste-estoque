from django.db import models
from collection.models import Collection
from color.models import Color
from brand.models import Brand


class Stock(models.Model):

    name = models.CharField(max_length=200)
    barcode = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    images_0 = models.ImageField(upload_to='media/', blank=True, null=True)
    images_1 = models.ImageField(upload_to='media/', blank=True, null=True)
    images_2 = models.ImageField(upload_to='media/', blank=True, null=True)
    images_3 = models.ImageField(upload_to='media/', blank=True, null=True)
    price = models.CharField(blank=True, null=True, max_length=200)
    quantity = models.CharField(max_length=13, blank=True, null=True)
    color = models.ManyToManyField(Color , related_name='stocks')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    collections = models.ManyToManyField(Collection, related_name='collections')
    variations = models.CharField(max_length=200, blank=True, null=True) 
    number_active = models.BooleanField(default=True)
    size_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
