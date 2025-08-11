from django.urls import path
from api.views import IncomeListCreateView, IncomeRetrieveUpdateDestroyView, ExpenseListCreateView, ExpenseRetrieveUpdateDestroyView


urlpatterns = [
    path('incomes/', IncomeListCreateView.as_view(), name='income-list-create'),
    path('incomes/<int:id>/', IncomeRetrieveUpdateDestroyView.as_view(), name='income-update-destroy'),
    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list-create'),
    path('expenses/<int:id>/', ExpenseRetrieveUpdateDestroyView.as_view(), name='expense-update-destroy'),
]