from rest_framework import serializers

from .models import User_Info

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Info
        fields = (
            "id",
            "firstName",
            "lastName",
            "phone",
            "address",
            "get_image"
        )

class UserInfoUpdatable(serializers.ModelSerializer):
    class Meta:
        model = User_Info
        fields = (
            "firstName",
            "lastName",
            "phone",
            "address",
            "image"
        )
