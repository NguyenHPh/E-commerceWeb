from django.urls import path, include

from products import views

urlpatterns = [
    path('collections', views.CategoryList.as_view()),
    path('collections/all', views.ProductsList.as_view()),
    path('collections/<slug:category_slug>/', views.CategoryDetail.as_view()),
    path('collections/<slug:category_slug>/all', views.Products_Category.as_view()),
    path('collections/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    # path('collections/all/search/', views.search),
    # path('collections/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    # path('collections/<slug:category_slug>/', views.CategoryDetail.as_view()),
]