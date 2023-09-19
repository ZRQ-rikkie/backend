from django.db import models

# Create your models here.

class Collection(models.Model):
    title = models.CharField(max_length=255)

class Product(models.Model):
    title = models.CharField(max_length =255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    iventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now_add=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)

class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]
    first_name = models.CharField(max_length =255)
    last_name = models.CharField(max_length =255)
    email = models.EmailField(unique=True)
    phone = models.CharFieldField(max_length =255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices = MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)

class Order(models.Model):
    STATUS_PENDING = 'P'
    STATUS_COMPLETE = 'C'
    STATUS_FAILD = 'F'
    PAYMENT_STATUS =[
        (STATUS_PENDING,'pending'),
        (STATUS_COMPLETE,'complete'),
        (STATUS_FAILD,'faild'),
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1,choices=PAYMENT_STATUS,default=STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    # customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)



class OrderItem(models.Model):
    order = models.ForeignKey(Collection, on_delete=models.PROTECT)
    product = models.ForeignKey(Collection, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DateTimeField(max_digits=6, decimal_places=2)
    cart = models.ForeignKey(Collection, on_delete=models.CASCADE)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()