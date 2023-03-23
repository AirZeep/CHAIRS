from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('market', views.market, name='market'),
    path('cart', views.cart, name="cart"),
    path('userinformation', views.userinformation, name="userinformation"),
    path('insert_user_info', views.insert_user_info, name="insert_user_info"),
    path('update_item', views.update_item, name="update_item")
]