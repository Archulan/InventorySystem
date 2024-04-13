from django.db import models

class ItemType(models.Model):
    type_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.type_name
