from datetime_utils.date_time import DateTime
from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateField(default=DateTime.datenow)
    updated_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name