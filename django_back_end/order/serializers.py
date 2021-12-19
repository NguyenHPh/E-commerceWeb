from rest_framework import serializers

from .models import OrderItem, Order

from products.serializers import ProductSerializer


class MyOrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = {
            "product",
            "price",
            "quantity"
        }


class MyOrderSerializer(serializers.ModelSerializer):

    items = MyOrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "firstname",
            "lastname",
            "email",
            "phone",
            "address",
            'created_at',
            "paid_amount",
            "stripe_token",
            "items",
            "paid_amount"
        )


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = {
            "product",
            "price",
            "quantity"
        }


class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "firstname",
            "lastname",
            "email",
            "phone",
            "address",
            'created_at',
            "paid_amount",
            "stripe_token",
            "items"
        )

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)

        return order
