from django.db import models


class Collection(models.Model):
    name_collection = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name_collection
