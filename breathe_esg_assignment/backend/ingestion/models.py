from django.db import models

class EmissionRecord(models.Model):
    source_type = models.CharField(max_length=50)
    scope = models.CharField(max_length=20)
    category = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=20)
    co2e = models.FloatField()
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)