from rest_framework import serializers
from .models import *


class PrgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    progress = PrgressSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ("id", "client", "title", "description",
                  "status", "waiter", "assigned_to", "created_at", "progress")
