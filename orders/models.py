from django.db import models
from clients.models import Client
from users.models import CustomUser
STATUS_CHOICES = (
    ('New', 'New'),
    ('Preparing', 'Preparing'),
    ('Waiting Review', 'Waiting Review'),
    ('Ready', 'Ready'),
    ('Canceled', 'Canceled')
)


class Order(models.Model):
    client = models.ForeignKey(
        Client, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders'
    )
    title = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES,
                              max_length=50, default='New')
    assigned_to = models.ForeignKey(
        CustomUser, null=True, blank=True, on_delete=models.SET_NULL, related_name="orders")


class Progress(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, blank=True, related_name='progress'
    )
    date_time = models.DateField(auto_now=True)
