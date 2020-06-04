from django.shortcuts import render
from .models import Category,Product
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView,CreateView
from django.urls import reverse_lazy



class ProductListView(ListView):
    model = Product
    template_name = 'shop/shop_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/shop_detail.html'


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'shop/shop_edit.html'
    fields = ('name','description')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'shop/shop_delete.html'
    success_url = reverse_lazy('product:product_list')


class ProductCreateView(CreateView):
    model = Product
    template_name = 'shop/shop_create.html'
    fields = ('name','category','description','price','quantity')
    success_url = reverse_lazy('product:product_list')