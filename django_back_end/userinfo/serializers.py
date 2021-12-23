from rest_framework import serializers

from .models import User_Info

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Info
        fields = (
            "user",
            "firstName",
            "lastName",
            "phone",
            "address"
        )

class UserInfoUpdatable(serializers.ModelSerializer):
    class Meta:
        model = User_Info
        fields = (
            "firstName",
            "lastName",
            "phone",
            "address"
        )
