from django.http import response
from django.shortcuts import render
from rest_framework import serializers
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User

# Create your views here.


class ViewUserList(APIView):
    def get(self, request, format=None):
        users = User.objects.all()[0:4]
        serializers = UserSerializer(users, many=True)
        return Response(serializers.data)
