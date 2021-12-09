from rest_framework import serializers

from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "category",
            "brief_component",
            "tray1",
            "quantity1",
            "tray2",
            "quantity2",
            "tray3",
            "quantity3",
            "lifeStage",
            'labelrange',
            "front_image",
            "pic1",
            "pic2",
            "pic3",
            "pic4",
            "pic5",
            "description",
            "nutrition_info",
            "feeding_guide",
            "deliver_info", 
            "rating",
            "get_absolute_url"
         )

class CategorySerializer(serializers.ModelSerializer):
    # products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "description",
            'get_image',
            "get_absolute_url"
            # "products",
        )  
