from django.urls import path
from .views import ExpenseChoicesView, IncomeChoicesView, CategoriesView

urlpatterns = [
    path("expences/", ExpenseChoicesView.as_view(), name="expenses-static-endpoint"),
    path("incomes/", IncomeChoicesView.as_view(), name="incomes-static-endpoint"),
    path("", CategoriesView.as_view(), name="categories-static-endpoint")
]