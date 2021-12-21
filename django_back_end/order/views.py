from django.shortcuts import render
import stripe

from django.contrib.auth.models import User
from django.conf import settings
from django.http import Http404, response

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from stripe.api_resources import charge, source

from .models import Order, OrderItem
from .serializers import OrderSerializer, MyOrderSerializer



@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkOut(request):
    serializer = OrderSerializer(data=request.data)
    if(serializer.is_valid()): 
        try:
            serializer.save(user=request.user)
            return Response({}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrdersList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders, many=True)
        print(serializer.data)
        return Response(serializer.data)
