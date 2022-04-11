from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from myshop.models import Product, Shop, Category
from shop_api.serializers import ProductSerializer


class ProductListView(APIView):
    def get(self, request, *args, **kwargs):
        objects = Product.objects.filter(shop=kwargs['shop'], category=kwargs['category'])
        serializer = ProductSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            shop = Shop.objects.get(pk=kwargs['shop'])
            category = Category.objects.get(pk=kwargs['category'])
            product = serializer.save(shop=shop, category=category)
            return Response(serializer.data)


class ProductView(APIView):
    def get(self, request, *args, **kwargs):
        product = Product.objects.get(pk=kwargs['product'])
        serializer = ProductSerializer(product)
        return Response(serializer.data)