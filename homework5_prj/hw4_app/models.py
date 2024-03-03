from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=256)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=256)
    registration_date = models.DateField()

    def __str__(self):
        return f' {self.name}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    product_count = models.IntegerField()
    added_at = models.DateField()

    def __str__(self):
        return f'{self.name}'


class ProductImage(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img/')


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateField()

    def __str__(self):
        return f'{self.created_at}. {self.total_price}'
