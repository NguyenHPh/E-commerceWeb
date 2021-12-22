from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class ProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            catename = Category.objects.get(slug = category_slug)
            return Product.objects.filter(category = catename).get(slug = product_slug)
            # return Product.objects.get(slug = productname.slug)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class CategoryList(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug = category_slug)
        except Category.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, format=None):
        Category = self.get_object(category_slug)
        serializer = CategorySerializer(Category)
        return Response(serializer.data)


class Products_Category(APIView):
    def get_object(self, category_slug):
        try:
            catename = Category.objects.get(slug = category_slug)
            return Product.objects.filter(category = catename)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, format=None):
        Product = self.get_object(category_slug)
        serializer = ProductSerializer(Product, many=True)
        return Response(serializer.data)


class search(APIView):
    def get(self, request, search_query, format=None):
        print(search_query)
        if search_query:
            print("yes")
            products = Product.objects.filter(Q(brief_component__icontains=search_query) | Q(special_range__icontains=search_query))
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        else:
            return Response({"products": []})
