from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from backend.authentication import TelegramAuthentication
from rest_framework.response import Response
from api.models import Expense, Income
from .handlers import statistics, visualization
from django.http import HttpResponse, StreamingHttpResponse
import io
import zipfile


class StatsView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TelegramAuthentication]

    def get(self, request, *args, **kwargs):
        expenses = Expense.objects.filter(user=self.request.user).values()
        incomes = Income.objects.filter(user=self.request.user).values()
        if not expenses or not incomes or expenses is None or incomes is None:
            return Response(data=None)
        results = {
            "expenses": list(expenses),
            "incomes": list(incomes)
        }
        return Response(data=statistics(data=results))



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

        plots_bytes_list = visualization(data=data_for_viz)

        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for i, plot_bytes in enumerate(plots_bytes_list):
                zip_file.writestr(f'report_{i + 1}.png', plot_bytes)

        zip_buffer.seek(0)
        response = StreamingHttpResponse(
            zip_buffer,
            content_type='application/zip'
        )
        response['Content-Disposition'] = 'attachment; filename="financial_report.zip"'
        return response