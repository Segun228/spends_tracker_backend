from django.urls import path
from .views import ListCreateAPIView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path("user/", ListCreateAPIView.as_view(), name="user-list-create-endpoint"),
    path("user/<int:pk>", UserRetrieveUpdateDestroyView.as_view(), name="user-retrieve-update-destroy-endpoint"),
]