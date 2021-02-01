from django.db import models
from django.contrib.auth.models import AbstractUser

USER_CHOICES = (
    ('CHIEF', 'Chief'),
    ('ASSISTANT', 'Assistant'),
    ('WAITER', 'Waiter'),
    ('CLIENT', 'client')
)


class CustomUser(AbstractUser):
    user_type = models.CharField(choices=USER_CHOICES, max_length=50)


class Chief(models.Model):
    user = models.OneToOneField(
        CustomUser, primary_key=True, on_delete=models.CASCADE)
    is_client_admin = models.BooleanField(default=False)
    max_time_minutes = models.PositiveIntegerField(default=0)


class Assistant(models.Model):
    user = models.OneToOneField(
        CustomUser, primary_key=True, on_delete=models.CASCADE)


class Waiter(models.Model):
    user = models.OneToOneField(
        CustomUser, primary_key=True, on_delete=models.CASCADE)
