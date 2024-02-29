from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from hw4_app.models import Client, Product, Order, ProductImage
from hw4_app.forms import ProductEditForm, ImageForm
from datetime import date, timedelta


def index(request):
    return render(request, 'hw4_app/base.html')


def clients(request):
    clients_list = Client.objects.all()
    context = {
        'length': len(clients_list),
        'clients': clients_list,
    }
    return render(request, 'hw4_app/clients.html', context)


def products(request):
    products_list = Product.objects.all()
    context = {
        'length': len(products_list),
        'products': products_list,
    }
    return render(request, 'hw4_app/products.html', context)


def client_orders(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client_id=client_id).order_by('-created_at')
    orders_last_week = [order for order in orders if order.created_at > (date.today() - timedelta(days=7))]
    orders_last_month = [order for order in orders if order.created_at > (date.today() - timedelta(days=30))]
    orders_two_years = [order for order in orders if order.created_at > (date.today() - timedelta(days=730))]
    # orders = Order.objects.filter(client=client).order_by('-created_at')
    # orders_last_week = Order.objects.filter(client=client, created_at__gte=date.today() - timedelta(days=7))
    # orders_last_month = Order.objects.filter(client=client, created_at__gte=date.today() - timedelta(days=30))
    # orders_two_years = Order.objects.filter(client=client, created_at__gte=date.today() - timedelta(days=730))

    context = {
        'orders': orders,
        'week': orders_last_week,
        'month': orders_last_month,
        'year_2': orders_two_years,
        'client': client,
    }
    return render(request, 'hw4_app/client-orders.html', context)


def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'hw4_app/order.html', {'order': order})


def product_edit(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product_images = ProductImage.objects.filter(product_id=product).all()
    if request.method == 'POST':
        form = ProductEditForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            product.name = data['name']
            product.description = data['description']
            product.price = data['price']
            product.product_count = data['product_count']
            product.added_at = data['added_at']
            product.save()
            # return redirect('products', product_id)
            return redirect('products')
    else:
        form = ProductEditForm(initial={
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'product_count': product.product_count,
            'added_at': product.added_at,
        })

    context = {
        'images': product_images,
        'product': product,
        'form': form,
    }
    return render(request, 'hw4_app/product-edit.html', context)


def upload_image(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(new_image.name, new_image)
            ProductImage.objects.create(
                product_id=product,
                image=new_image,
            )
            return redirect('product_edit', product_id)
    else:
        form = ImageForm()

    context = {
        'product': product,
        'form': form,
    }
    return render(request, 'hw4_app/upload_image.html', context)
