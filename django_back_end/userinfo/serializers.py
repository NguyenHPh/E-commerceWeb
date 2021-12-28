from rest_framework import serializers

from .models import User_Info
from django.contrib.auth.models import User
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Info
        fields = (
            "firstName",
            "lastName",
            "phone",
            "address"
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields=('__all__')
        fields=(
            "id",
            "email",
            "username"
        )
