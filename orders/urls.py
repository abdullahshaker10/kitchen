
from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('api/create', OrderCreate.as_view(), name='create-order'),
    path('api', OrderList.as_view(), name='list-orders'),
]
