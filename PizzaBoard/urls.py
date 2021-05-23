from .views import *
from django.urls import path

urlpatterns = [
    path('pizzas', PizzaList.as_view(), name='pizza_list'),
    path('pizzas/<int:pk>', PizzaDetailView.as_view(), name='pizza'),
    path('make-order', make_order, name='order_page'),
    path('orders', OrdersList.as_view(), name='orders_list'),
]

