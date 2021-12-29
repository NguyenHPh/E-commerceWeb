from django.urls import path, include
from userinfo import views

urlpatterns = [
    path('userinfo', views.ViewUserInfo.as_view()),
    path('userorderinfo', views.ViewUserOrderInfo.as_view()),
    path('updateinfo', views.updateInfo),
]
