from django.db import models
from users.models import CustomUser


class Client(models.Model):
    user = models.OneToOneField(
        CustomUser, primary_key=True, on_delete=models.CASCADE)
    logo_png = models.ImageField(null=True, blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)
