from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import EXPENSE_CHOICES_LIST, INCOME_CHOICES_LIST

CATEGORIES = {
    "expenses": EXPENSE_CHOICES_LIST,
    "incomes": INCOME_CHOICES_LIST
}
class ExpenseChoicesView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(data=EXPENSE_CHOICES_LIST)


class IncomeChoicesView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(data=INCOME_CHOICES_LIST)


class CategoriesView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(data=CATEGORIES)
