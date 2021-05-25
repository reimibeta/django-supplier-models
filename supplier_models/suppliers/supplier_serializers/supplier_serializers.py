from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from supplier_models.suppliers.models import Supplier


class SupplierSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Supplier
        # exclude = ('removed_by',)
        fields = [
            'id',
            'url',
            'name',
            'created_date',
            'updated_date',
            'is_active'
        ]
        expandable_fields = {}
