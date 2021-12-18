from rest_framework import serializers

from .models import User_Info


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Info
        fields = (
            "id",
            "firstName",
            "lastName",
            "email",
            "password",
            "image"
        )
