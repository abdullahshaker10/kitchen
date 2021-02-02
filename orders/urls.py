
from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('api/create', OrderCreate.as_view(), name='create-order'),
    path('api/details/<int:pk>', OrderDetails.as_view(), name='order-details'),
    path('api/<int:pk>', OrderList.as_view(), name='list-orders'),
    path('api/update/<int:pk>', OrderUpdate.as_view(), name='update-order'),
    path('progress/api/create', PrgressCreate.as_view(), name='create-progress'),
    path('progress/api/<int:pk>', ProgressList.as_view(), name='list-progress'),

]
