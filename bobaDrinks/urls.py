from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('orderForm', views.orderForm, name='orderForm'),
    path('orderHistory', views.orderHistory, name='orderHistory'),
    path('thanks', views.thanks, name='thanks'),
]