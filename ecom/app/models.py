from django.db import models

class UserProfile(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def str(self):
        return self.email

class Order(models.Model):
    order_id = models.CharField(max_length=50, unique=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    
    def str(self):
        return self.order_id

class Delivery(models.Model):
    delivery_id = models.CharField(max_length=50, unique=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    
    def str(self):
        return self.delivery_id

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    rating = models.FloatField(default=0.0)
    quantity = models.PositiveIntegerField()

    def _str_(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='brands/')

    def _str_(self):
        return self.name