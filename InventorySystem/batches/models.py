from django.db import models
from items.models import Item

class Batch(models.Model):
    batch_code = models.CharField(max_length=100)
    date_received = models.DateField()
    quantity = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='batches')

    def __str__(self):
        return self.batch_code
