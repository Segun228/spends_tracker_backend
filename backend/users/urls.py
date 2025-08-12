from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path("user/", UserListCreateView.as_view(), name="user-list-create-endpoint"),
    path("user/<str:telegram_id>/", UserRetrieveUpdateDestroyView.as_view(), name="user-retrieve-update-destroy-endpoint"),
]