from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework_utils.pagination import StandardResultsSetPagination

from supplier_models.suppliers.models import Supplier
from supplier_models.suppliers.supplier_serializers.supplier_serializers import SupplierSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = SupplierSerializer
