from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Chairs, UserInformation, Order


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def market(request):
    chairs = Chairs.objects.all()
    return render(request, 'main/market.html', {'chairs': chairs})


def cart(request):
    amount = 0
    total_price = 0
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        amount = 0
        total_price = 0
        for i in items:
            total_price += i.chair.price * i.quantity
            amount += i.quantity
    else:
        items = []
    return render(request, 'main/cart.html', {'items': items, 'amount': amount, 'total_price': total_price})


def userinformation(request):
    form = UserInformation(request.POST)
    return render(request, 'main/userinformation.html', {'form': form})


def insert_user_info(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        city = request.POST['city']
        street = request.POST['street']
        house = request.POST['house']
        floor = request.POST['floor']
        apartment = request.POST['apartment']

        userinfo = UserInformation(name=name, phone_number=phone_number, mail=email, city=city, street=street,
                                   house=house, floor=floor, apartment=apartment)
        userinfo.save()
        return HttpResponse("Data Saved")
    else:
        return render(request, 'main/userinformation.html')


def update_item(request):
    return JsonResponse('Item was added', safe=False)