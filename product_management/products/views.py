from rest_framework import viewsets
from rest_framework import permissions
from product_management.products.models import Product
from product_management.products.serializers import ProductSerializer, ProductSerializerPublic


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return ProductSerializer
        return ProductSerializerPublic

    def get_permissions(self):
        if self.action in ('create', 'update', 'delete'):
            return [permissions.IsAuthenticated(), self.request.user.is_staff]
        return super().get_permissions()
