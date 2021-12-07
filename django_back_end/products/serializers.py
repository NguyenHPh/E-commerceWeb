from rest_framework import serializers

from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "category",
            "head_title",
            "brief_component",
            "price_before",
            "price_after",
            "lifeStage",
            "front_image",
            "thumbnail_front_image",
            "product_detail_images",
            "meta_data",
            "get_absolute_url"
         )

class CategorySerializer(serializers.ModelSerializer):
    # products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "description"
            "slug"
            # "products",
        )  