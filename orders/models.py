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
    waiter = models.ForeignKey(
        CustomUser, null=True, blank=True, on_delete=models.SET_NULL, related_name="recived_orders")
    assigned_to = models.ForeignKey(
        CustomUser, null=True, blank=True, on_delete=models.SET_NULL, related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        ordering = ("created_at",)


class Progress(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, blank=True, related_name='progress'
    )
    progress_note = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='progress')

    class Meta:
        ordering = ("created_at",)
