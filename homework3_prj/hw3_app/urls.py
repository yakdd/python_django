from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.clients, name='clients'),
    path('client/<int:client_id>', views.client_orders, name='client_orders'),
    path('order/<int:order_id>', views.order_detail, name='order_detail'),
]
