from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('api/update/<int:pk>', UserUpdate.as_view(), name='user-update'),
]
