from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from orders.permissions import IsChiefAndAdmin
from rest_framework.response import Response


class UserUpdate(generics.UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsChiefAndAdmin]
    queryset = CustomUser.objects.all()
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        data = self.request.data
        instance = self.get_object()
        instance.is_active = data['active']
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
