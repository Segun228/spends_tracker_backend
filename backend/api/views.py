from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Income, Expense
from .serializers import (
    IncomeSerializer,
    ExpenseSerializer
)

from backend.authentication import TelegramAuthentication



class IncomeListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TelegramAuthentication]
    serializer_class = IncomeSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        current_user = self.request.user
        return Income.objects.filter(user= current_user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class IncomeRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [TelegramAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'




class ExpenseListCreateView(ListCreateAPIView):
    authentication_classes = [TelegramAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ExpenseSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        current_user = self.request.user
        return Expense.objects.filter(user= current_user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ExpenseRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [TelegramAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
