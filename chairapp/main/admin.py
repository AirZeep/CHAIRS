from django.contrib import admin
from .models import Chairs, UserInformation, Customer, Order, OrderItem

admin.site.register(Customer)
admin.site.register(Chairs)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(UserInformation)
