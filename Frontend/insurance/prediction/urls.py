from django.conf.urls import url,include
from django.contrib import admin
from .import views

urlpatterns = [
    #url for homepage:
    url(r'^$',views.index,name="index"),
    #for customerlist
    url(r'^customer/$',views.customerList.as_view(),name="customerList"),
    #url for customer detail:
    url(r'^customer/(?P<customer_id>[0-9]+)/$',views.customerInfo, name="customerInfo"),
    #form
    url(r'^customer/add/$', views.customerCreate.as_view(), name = "customerCreate"),

]
