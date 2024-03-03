from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.clients, name='clients'),
    path('products/', views.products, name='products'),
    path('client/<int:client_id>', views.client_orders, name='client_orders'),
    path('order/<int:order_id>', views.order_detail, name='order_detail'),
    path('product_edit/<int:product_id>', views.product_edit, name='product_edit'),
    path('upload_image/<int:product_id>', views.upload_image, name='upload_image'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
