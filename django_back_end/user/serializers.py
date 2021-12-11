from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

<<<<<<< HEAD
# User Serializer
=======
from .models import User_Info
>>>>>>> 51342fed9b79816469c4d018bd77328344325ca7


class UserSerializer(serializers.ModelSerializer):
    class Meta:
<<<<<<< HEAD
        model = User
        fields = ('username', 'email', 'password')

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            Token.objects.create(user=user)
            return user

            # Register Serializer
=======
        model = User_Info
        fields = (
            "id",
            "firstName",
            "lastName",
            "email",
            "password",
            "subcribe"
        )
>>>>>>> 51342fed9b79816469c4d018bd77328344325ca7
