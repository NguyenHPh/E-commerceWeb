from django.urls import path, include
from order import views

urlpatterns = [
    path('checkout/', views.checkOut),
    path('orders/', views.OrdersList.as_view())  
]
