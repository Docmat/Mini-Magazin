from django.urls import path
from .views import (
    ProductListView,
    ProductUpdateView,
    ProductDetailView,
    ProductDeleteView,)




urlpatterns = [
    path('',ProductListView.as_view(),name = 'product_list'),
    path('product/<int:pk>/edit/',ProductUpdateView.as_view(),name='product_edit'),
    path('product/<int:pk>/',ProductDetailView.as_view(),name='product_detail'),
    path('product/<int:pk>/delete/',ProductDeleteView.as_view(),name='product_delete'),
  

]


