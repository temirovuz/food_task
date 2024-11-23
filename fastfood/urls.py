from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from fastfood.views import CreateFood, FoodRetrieveUpdateDestroyView, OrderListView, OrderCreateView

urlpatterns = [
    path('foods/', CreateFood.as_view(), name='food-list-create'),
    path('foods/<int:pk>/', FoodRetrieveUpdateDestroyView.as_view(), name='food-detail'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/create/', OrderCreateView.as_view(), name='order-create'),
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

