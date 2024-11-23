from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from fastfood.models import FoodMeny, Order
from fastfood.permissions import IsAdminOrWaiter
from fastfood.serializers import FoodSerializer, OrderSerializer, OrderCreateSerializer


class CreateFood(generics.ListCreateAPIView):
    queryset = FoodMeny.objects.all()
    serializer_class = FoodSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated(), IsAdminOrWaiter()]
        return [AllowAny()]


class FoodRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodMeny.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated(), IsAdminOrWaiter()]


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated()]

    def get_queryset(self):
        if hasattr(self.request.user, 'role') and self.request.user.role == 'user':
            return self.queryset.filter(user=self.request.user)
        return self.queryset


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer
    permission_classes = [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
