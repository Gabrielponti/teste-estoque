from django.db import models


class Brand(models.Model):
    name_brand = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name_brand
