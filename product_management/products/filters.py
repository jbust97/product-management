import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    in_stock = django_filters.ChoiceFilter(choices=((0, False), (1, True)))
    category = django_filters.CharFilter(field_name='categories__name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = []
