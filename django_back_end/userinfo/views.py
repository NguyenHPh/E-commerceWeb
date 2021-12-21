import stripe

from django.conf import settings

from django.http import Http404
from django.shortcuts import render
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView

from rest_framework.response import Response

from django.contrib.auth.models import User
from .models import User_Info
from .serializers import UserInfoSerializer

# class ViewUserList(APIView):
#     def get(self, request, format=None):
#         users = User_Info.objects.all()
#         serializers = UserSerializer(users, many=True)
#         return Response(serializers.data)

class ViewUserInfo(APIView):
    def get(self, request, format=None):
        users = User_Info.objects.all()
        serializers = UserInfoSerializer(users, many=True)
        return Response(serializers.data)


# user = User.objects.get(id=2)
# user_email = user.email

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def updateInfo(request, pk):
    serializer = UserInfoSerializer(data=request.data)

    if serializer.is_valid():
        # stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
