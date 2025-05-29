from django.db import models


# Create your models here.
class Color(models.Model):
    name_color = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name_color
