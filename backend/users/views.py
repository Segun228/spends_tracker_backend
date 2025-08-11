from .models import User
from .serializers import UserSerializer
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()