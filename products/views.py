import random
import string
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import user_logged_in
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
import datetime
from .models import Product, Orderproduct, Orders, OrderProductrel,Productcategory, Productinventory, AuthUser
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, View
from .forms import OrderForm, OrderItemForm
from .filters import OrderHistoryFilter

# Create your views here.

#def product_detail_view(request):
#    obj = Product.objects.get(productid='A225489')
#    context = {
#       'name': obj.name, 
#       'model': obj.model,
#       'rentalcost': obj.rentalcost,
#       'weight': obj.weight
#   }    
#    return render(request, "products/products_detail.html", context)

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset,
    
    }
    return render(request, "products/product_list.html", context)



class order_history_view(ListView):
    model = Orders
    template_name = 'products/order_history.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = OrderHistoryFilter(self.request.GET, queryset=self.get_queryset())
        return context




@login_required
def order_item_view(request):
    form = OrderItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = OrderItemForm()
        return redirect('create-order')
    context = {
        'form': form
    }
    return render(request, "products/order_item.html", context)
    


@login_required
def create_order_view(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = OrderForm()
        return redirect('quote')
    context = {
        'form': form
       
    }
    return render(request, "products/order_create.html", context)

@login_required
def PriceView(request):
    queryset = Orderproduct.objects.all()
    context = {
        "object_list": queryset,

    }
    return render(request, "products/quote.html", context)



#@login_required
#def create_order_view(request):
#    my_form = RawOrderForm()
#    if request.method == "POST":
#        my_form = RawOrderForm(request.POST)
#        if my_form.is_valid():
#            print(my_form.cleaned_data)
#            Orders.objects.create(**my_form.cleaned_data)
#        else:
#            print(my_form.errors)
#    context = {
#        "form": my_form
#    }
#    return render(request, "products/order_create.html", context)


