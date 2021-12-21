from rest_framework import serializers

from .models import OrderItem, Order

from products.serializers import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = (
            "product",
            "quantity",
            "trayQuantity",
            "trayPricePer",
            "price",
        )


class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            "first_name",
            "last_name",
            "phone",
            "address",
            'created_at',
            "paid_amount",
            "items",
        ]

    def create(self, data):
        items_data = data.pop("items")
        order = Order.objects.create(**data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order



class MyOrderItemSerializer(serializers.ModelSerializer):    
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = (
            "product",
            "quantity",
            "trayQuantity",
            "trayPricePer",
            "price",
        )

class MyOrderSerializer(serializers.ModelSerializer):
    # items = MyOrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            "first_name",
            "last_name",
            "phone",
            "address",
            'created_at',
            "paid_amount",
            # "items",
        ]

