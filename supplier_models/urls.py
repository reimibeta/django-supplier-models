from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from supplier_models import views

router = routers.DefaultRouter()
""" supplier api """
router.register('supplier', views.SupplierViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
