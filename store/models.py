from django.db import models

MEMBERSHIP_BRONZE = 'B'
MEMBERSHIP_SILVER = 'S'
MEMBERSHIP_GOLD = 'G'

MEMPERSHIP_CHOICES = [
    (MEMBERSHIP_BRONZE , 'BRONZE'),
    (MEMBERSHIP_SILVER , 'SILVER'),
    (MEMBERSHIP_GOLD , 'GOLD'),
]

PAYMENT_STATUS_PENDING = 'P'
PAYMENT_STATUS_COMPLETE = 'C'
PAYMENT_STATUS_FAILED = 'F'

PAYMENT_STATUS_CHOICES = [
    (PAYMENT_STATUS_PENDING , 'PENDING'),
    (PAYMENT_STATUS_COMPLETE , 'COMPLETE'),
    (PAYMENT_STATUS_FAILED , 'FAILED'),

]

# Create your models here.
class Collection(models.Model):
    title = models.CharField( max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL,null=True,related_name='+')
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    unite_price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection,on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1,choices=MEMPERSHIP_CHOICES,default=MEMBERSHIP_BRONZE)

    class Meta:
        indexes = [
            models.Index(fields=['last_name','first_name'])
        ]


class Cart(models.Model):
    created_at = models.DateField(auto_now_add=True)

class Order(models.Model):
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1,choices=PAYMENT_STATUS_CHOICES,default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    
class Adress(models.Model):
    zip = models.CharField(max_length=10,default='00000')
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)

