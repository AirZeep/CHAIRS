from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField('Customer Name', max_length=100)

    def __str__(self):
        return self.name


class Chairs(models.Model):
    chair_name = models.CharField('Chair name', max_length=100)
    price = models.IntegerField('Price')
    pic = models.ImageField('Picture', upload_to='static/main/img/')
    mini_pic = models.ImageField('Small Picture', upload_to='static/main/img/', default="null")

    def __str__(self):
        return self.chair_name

    class Meta:
        verbose_name = 'Chair'
        verbose_name_plural = 'Chairs'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField("Date Ordered", auto_now_add=True)
    complete = models.BooleanField("Complete",default=False, null=True, blank=False)
    transaction_id = models.CharField('Transaction', max_length=200)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderItem(models.Model):
    chair = models.ForeignKey(Chairs, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField('Quantity')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Order_Item'
        verbose_name_plural = 'Order_Items'


CITY_CHOICES = (
    ('spb', 'Saint-Petersburg'),
    ('msk', 'Moscow'),
    ('smr', 'Samara'),
    ('kzn', 'Kazan'),
)


class UserInformation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField('User Name', max_length=100)
    phone_number = PhoneNumberField(unique=True, null=False, blank=False)
    mail = models.EmailField('E-mail')
    city = models.CharField(max_length=25, choices=CITY_CHOICES, default='green')
    street = models.CharField('Street', max_length=100)
    house = models.IntegerField('House')
    floor = models.IntegerField('Floor')
    apartment = models.IntegerField('Apartment')
    comment = models.TextField('Comment')

    class Meta:
        verbose_name = 'UserInfo'
        verbose_name_plural = 'UserInfos'
