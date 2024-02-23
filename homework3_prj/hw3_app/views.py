from django.shortcuts import render, get_object_or_404
from hw3_app.models import Client, Product, Order
from datetime import date, timedelta


def index(request):
    return render(request, 'hw3_app/base.html')


def clients(request):
    clients_list = Client.objects.all()
    context = {
        'length': len(clients_list),
        'clients': clients_list,
    }
    return render(request, 'hw3_app/clients.html', context)


def client_orders(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client_id=client_id).order_by('-created_at')
    orders_last_week = [order for order in orders if order.created_at > (date.today() - timedelta(days=7))]
    orders_last_month = [order for order in orders if order.created_at > (date.today() - timedelta(days=30))]
    orders_two_years = [order for order in orders if order.created_at > (date.today() - timedelta(days=730))]
    context = {
        'orders': orders,
        'week': orders_last_week,
        'month': orders_last_month,
        'year_2': orders_two_years,
        'client': client,
    }
    return render(request, 'hw3_app/client-orders.html', context)


def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'hw3_app/order.html', {'order': order})
