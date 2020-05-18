from django.urls import path
from .views import ShopPageView

urlpatterns = [
    path('shop/',ShopPageView.as_view(),name = 'shop_list'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)