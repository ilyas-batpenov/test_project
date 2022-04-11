from django.contrib import admin
from django.urls import path, include
from .views import ProductListView, ProductView

urlpatterns = [
    path('<int:shop>/categories/<int:category>/', ProductListView.as_view(), name='ProductListView'),
    path('<int:shop>/categories/<int:category>/<int:product_pk>', ProductView.as_view(), name='product_page'),


]