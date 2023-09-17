from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
from drf_yasg.utils import swagger_auto_schema

from .models import Product, Category
from .serializers import ProductSerializer, ProductSerializerPublic, CategorySerializer
from .filters import ProductFilter



class StaffPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated:
            return user.is_staff
        return False


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ProductFilter

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return ProductSerializer
        return ProductSerializerPublic

    def get_permissions(self):
        if self.action in ('create', 'update', 'delete'):
            return [StaffPermission()]
        return super().get_permissions()

    @swagger_auto_schema(
        request_body=ProductSerializer,  # Serializer for POST request
        responses={200: ProductSerializer},  # Serializer for GET response
    )
    def create(self,request):
        return super().create(request)

    @swagger_auto_schema(
        request_body=ProductSerializer,
        responses={200: ProductSerializer},
    )
    def update(self, request):
        return super().update(request)

    @swagger_auto_schema(
        request_body=ProductSerializer,
    )
    def destroy(self, request):
        return super().destroy(request)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [StaffPermission]

