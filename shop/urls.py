from django.urls import path
from .views import (
    ProductListView,
    ProductUpdateView,
    ProductDetailView,
    ProductDeleteView,)




urlpatterns = [
    path('',ProductListView.as_view(),name = 'product_list'),
    path('<int:pk>/edit/',ProductUpdateView.as_view(),name='product_edit'),
    path('<int:pk>/',ProductDetailView.as_view(),name='product_detail'),
    path('<int:pk>/delete/',ProductDeleteView.as_view(),name='product_delete'),
  

]


