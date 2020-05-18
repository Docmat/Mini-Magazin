from django.shortcuts import render
from .models import Category,Product
from django.views.generic import ListView


class ProductListView(ListView):
    model = Product
    template_name = 'shop_list.html'
