from rest_framework import serializers
from myshop.models import Shop, Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']

        # read_only_fields = ['category', 'shop']
