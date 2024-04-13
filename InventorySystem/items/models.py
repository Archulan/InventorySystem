from django.db import models
from itemtypes.models import ItemType

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()
    item_type = models.ForeignKey(ItemType, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.name
