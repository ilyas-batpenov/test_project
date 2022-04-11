from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from myshop.models import Product, Shop, Category
from shop_api.serializers import ProductSerializer
from rest_framework.pagination import PageNumberPagination


class ProductListView(APIView, PageNumberPagination):
    page_size = 5

    def get(self, request, *args, **kwargs):
        objects = Product.objects.filter(shop=kwargs['shop'],
                                         category=kwargs['category']).order_by('id')
        if request.query_params.get('page'):
            objects = self.paginate_queryset(objects, request)
        serializer = ProductSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            shop = Shop.objects.get(pk=kwargs['shop'])
            category = Category.objects.get(pk=kwargs['category'])
            serializer.save(shop=shop, category=category)
            return Response(serializer.data)


class ProductView(APIView):
    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs['product_pk'])
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs['product_pk'])
        # product.update_counter += 1
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)