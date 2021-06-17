from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django_rest_framework.pagination import StandardResultsSetPagination

from supplier_models.models import Supplier
from supplier_models.supplier_serializers.supplier_serializers import SupplierSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = SupplierSerializer
