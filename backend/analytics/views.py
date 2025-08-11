from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from backend.authentication import TelegramAuthentication
from rest_framework.response import Response
from api.models import Expense, Income
from .handlers import statistics, visualization
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse

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
        return Response(data=statistics(data= results))



class VisualView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TelegramAuthentication]

    def get(self, request, *args, **kwargs):
        expenses = Expense.objects.filter(user=self.request.user).values()
        incomes = Income.objects.filter(user=self.request.user).values()

        data_for_viz = {
            "expenses": list(expenses),
            "incomes": list(incomes)
        }

        image_bytes = visualization(data=data_for_viz)

        return HttpResponse(image_bytes, content_type='image/png')