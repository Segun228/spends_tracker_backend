from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import AllowAny

from .models import Income, Expense
from .serializers import (
    IncomeSerializer,
    ExpenseSerializer
)



class IncomeListCreateView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = IncomeSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    def get_queryset(self):
        current_user = self.request.user
        return Income.objects.filter(user= current_user)

class IncomeRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'




class ExpenseListCreateView(ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

class ExpenseRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
