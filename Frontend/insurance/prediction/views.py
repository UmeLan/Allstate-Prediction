from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import *
from django.template import loader
from django.shortcuts import render, get_object_or_404,redirect
from django.views import generic
from django.forms import ModelForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import admin


# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return render(request, 'index.html')

class customerList(generic.ListView):
    template_name = 'customerList.html'
    context_object_name = 'all_customer'
    def get_queryset(self):
        return Customer.objects.all().order_by('-id')

##view for detail page
def customerInfo(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    context = {'customer': customer}
    return render(request, 'customerInfo.html', context)

#create form
class customerCreate(CreateView):
    model = Customer
    fields = ['customer_ID','state_group','group_size',
              'homeowner','car_age','car_value','risk_factor',
              'married_couple','C_previous','duration_previous',
              'cost','timeofday','weekend','family','agedif','individual']

