from rest_framework import serializers
from myshop.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'update_counter']
        read_only_fields = ['update_counter']

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.update_counter += 1
        instance.save()
        return instance


