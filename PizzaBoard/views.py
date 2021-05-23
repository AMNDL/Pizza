from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Pizza, Order
from django.views.generic import ListView, DetailView
from PizzaBoard.forms import OrderForm
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from .services import *
from django.contrib.auth.decorators import login_required


# Create your views here.
class PizzaList(ListView):
    model = Pizza
    template_name = 'pizza_list.html'
    context_object_name = 'pizzas'


class OrdersList(ListView, LoginRequiredMixin):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'orders'


class PizzaDetailView(DetailView):
    template_name = 'pizza_detail.html'
    model = Pizza
    queryset = Pizza.objects.all()


@login_required()
def make_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            pizzas = form.cleaned_data.pop('pizzas')
            order_price = sum(list([float(pizza.price) for pizza in pizzas]))
            order = Order.objects.create(**form.cleaned_data, price=order_price)
            for pizza in pizzas:
                order.pizzas.add(pizza)
            return HttpResponseRedirect('/orders')
    else:
        form = OrderForm()
    return render(request, 'order_form.html', {'form': form})
