from django.urls import path, include
from user import views

urlpatterns = [
    path('list-user/', views.ViewUserList.as_view()),
]
