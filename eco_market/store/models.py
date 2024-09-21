from django.db import models
import datetime

#Categories of products
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

#Customers
class Customer(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phoneNo = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.firstName} {self.lastname}'
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(default= 0, max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/product/')

    def __str__(self):
        return self.name

#cCustomer orders
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    quantity = models.IntegerField(default =1)
    address = models.CharField(default='', max_length=100, blank = False)
    phone =  models.CharField(max_length=10)
    date = models.DateField(default=datetime.datetime.today)
    status =models.BooleanField(default=False)

    def __str__(self):
        return self.product
