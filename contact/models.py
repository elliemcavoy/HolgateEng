from django.db import models
import uuid

# Create your models here.

class Contact(models.Model):
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    request = models.CharField(max_length=1000, null=False, blank=False)
    ref_number = models.CharField(max_length=32, null=False, editable=False, default=0)
    
    def _generate_ref_number(self):
        
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        
        if not self.ref_number:
            self.ref_number = self._generate_ref_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.ref_number