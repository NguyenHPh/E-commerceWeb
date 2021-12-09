from rest_framework import serializers

from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "category",
            "special_range",
            "brief_component",
            "get_trays",
            "lifeStage",
            'labelrange',
            "front_image",
            "description",
            "nutrition_info",
            "feeding_guide",
            "deliver_info", 
            "rating",
            "get_image",
            "get_images_detail",
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
