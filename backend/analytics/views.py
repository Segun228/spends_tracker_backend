from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from backend.authentication import TelegramAuthentication
from rest_framework.response import Response
from api.models import Expense, Income
from .handlers import analizis
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class StatsView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TelegramAuthentication]

    def get(self, request, *args, **kwargs):
        expenses = Expense.objects.filter(user=self.request.user).values()
        incomes = Income.objects.filter(user=self.request.user).values()

        results = {
            "expenses": list(expenses),
            "incomes": list(incomes)
        }
        
        return Response(data=results)
