import stripe
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.shortcuts import render
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView

from rest_framework.response import Response

from django.contrib.auth.models import User
from .models import User_Info
from .serializers import UserInfoSerializer, UserSerializer


class ViewUserInfo(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        user = User.objects.get(id = request.user.id)
        serializers = UserSerializer(user)
        print(serializers)
        return Response(serializers.data)

class ViewUserOrderInfo(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        user = get_object_or_404(User_Info, user=request.user)
        serializers = UserInfoSerializer(user)
        print(serializers)
        return Response(serializers.data)


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def updateInfo(request):
    try:
        userinfo = User_Info.objects.get(user = request.user)
        serializer = UserInfoSerializer(instance = userinfo, data=request.data)
        if serializer.is_valid():
            print("ok")
            try:
                serializer.save(user = request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        print("No user found")
        print(request.data)
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            print("valid")
            try:
                serializer.save(user = request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
