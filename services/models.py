from django.db import models


# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name