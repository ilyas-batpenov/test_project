from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=100, verbose_name='Shop name')


class Category(models.Model):
    category = models.CharField(max_length=100, verbose_name='Category')


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Product name')
    category = models.ForeignKey('myshop.Category', on_delete=models.RESTRICT,
                                 related_name='products',
                                 verbose_name='Product category')
    shop = models.ForeignKey('myshop.Shop', on_delete=models.CASCADE, related_name='products',
                             verbose_name='Shop')
