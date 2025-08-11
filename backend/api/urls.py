from django.urls import path
from api.views import IncomeListCreateView, IncomeRetrieveUpdateDestroyView, ExpenseListCreateView, ExpenseRetrieveUpdateDestroyView


urlpatterns = [
    path('income/', IncomeListCreateView.as_view(), name='income-list-create'),
    path('income/<int:id>/', IncomeRetrieveUpdateDestroyView.as_view(), name='income-update-destroy'),
    path('expense/', ExpenseListCreateView.as_view(), name='expense-list-create'),
    path('expense/<int:id>/', ExpenseRetrieveUpdateDestroyView.as_view(), name='expense-update-destroy'),
]