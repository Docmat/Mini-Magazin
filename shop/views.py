from django.shortcuts import render,get_object_or_404
from .models import Category,Product
from django.views.generic import ListView

class ShopPageView(ListView):
    model = Product
    template_name = 'shop_list.html'
    