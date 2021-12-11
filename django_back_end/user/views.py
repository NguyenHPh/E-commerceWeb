<<<<<<< HEAD
from django.db.models import query
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

# Register API
=======

import stripe

from django.conf import settings

from django.http import Http404
from django.shortcuts import render
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView

from rest_framework.response import Response

from django.contrib.auth.models import User
from .serializers import UserSerializer
from .models import User_Info

class ViewUserList(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializers = UserSerializer(users, many=True)
        return Response(serializers.data)


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def updateInfo(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        # stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
>>>>>>> 51342fed9b79816469c4d018bd77328344325ca7
