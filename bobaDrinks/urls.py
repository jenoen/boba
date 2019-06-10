from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('orderForm', views.orderForm, name='orderForm'),
    path('orderHistory/<int:order_id>', views.orderHistory, name='orderHistory')
]