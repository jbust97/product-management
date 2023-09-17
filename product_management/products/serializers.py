from product_management.products.models import Category, Image, Product
from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    image_file = Base64ImageField(required=False)
    class Meta:
        model = Image
        fields = ['image_file']


class ProductSerializerPublic(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'in_stock']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    images = ImageSerializer(many=True, required=False)
    class Meta:
        model = Product
        fields = ['name', 'in_stock', 'categories', 'images']

    def create(self, validated_data):
        # Extract the 'images' data from the validated data
        images_data = validated_data.pop('images', [])

        # Create the product without images
        product = Product.objects.create(**validated_data)

        # Create associated images if provided
        for image_data in images_data:
            Image.objects.create(product=product, **image_data)

        return product


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'in_stock', 'categories']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
            latest_image = instance.images.latest('uploaded_at')
            data['latest_image'] = ImageSerializer(latest_image).data
        except Image.DoesNotExist:
            data['latest_image'] = None
        return data
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


