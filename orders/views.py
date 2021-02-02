from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import *
from rest_framework.response import Response


class OrderCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsWaiter]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def post(self, request, *args, **kwargs):
        body = request.data
        request.data["waiter"] = request.user.id
        return self.create(request, *args, **kwargs)


class OrderDetails(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderList(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = Order.objects.filter(
            client__pk=pk).exclude('progress').all()
        return queryset


class OrderUpdate(generics.UpdateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsAssitantOrChief]
    queryset = Order.objects.all()
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        data = self.request.data
        instance = self.get_object()
        instance.assigned_to = self.request.user
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class PrgressCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsAssitantOrChief]
    serializer_class = PrgressSerializer
    queryset = Progress.objects.all()

    def post(self, request, *args, **kwargs):
        body = request.data
        request.data["order"] = body['order']
        request.data["prgress_note"] = body['progress_note']
        request.data["created_by"] = request.user.id
        return self.create(request, *args, **kwargs)


class ProgressList(generics.ListAPIView):
    serializer_class = PrgressSerializer
    permission_classes = [IsAuthenticated, IsChief]

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = Progress.objects.filter(order__pk=pk).all()
        return queryset
