from product_management.products.models import Category, Image, Product
from rest_framework import serializers


class ProductSerializerPublic(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'in_stock']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'in_stock', 'categories']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name', ]
