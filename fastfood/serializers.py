from rest_framework import serializers

from fastfood.models import FoodMeny, Order, OrderItem


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodMeny
        fields = ('name', 'description', 'price', 'is_available')


class OrderItemSerializer(serializers.ModelSerializer):
    dish = FoodSerializer()

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    estimated_time = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'user', 'created_at', 'distance_to_customer',  'items', 'estimated_time']

    def get_estimated_time(self, obj):
        return obj.calculate_estimated_time()


class OrderCreateSerializer(serializers.ModelSerializer):
    items = serializers.ListField(child=serializers.DictField(), write_only=True)

    class Meta:
        model = Order
        fields = ['distance_to_customer', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order
