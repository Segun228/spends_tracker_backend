from rest_framework.serializers import ModelSerializer
from api.models import Expense, Income, INCOME_CHOICES, INCOME_CHOICES_LIST, EXPENSE_CHOICES, EXPENSE_CHOICES_LIST
from rest_framework import serializers


class ExpenseSerializer(ModelSerializer):
    class Meta:
        model = Expense
        fields = ["id", "title", "description", "value", "updated_at", "created_at", "category", "created_at"]
        read_only_fields = ["id", "updated_at"]
    def validate_category(self, value):
        if value not in EXPENSE_CHOICES_LIST:
            raise serializers.ValidationError(f"Категория '{value}' не является допустимой.")
        return value



class IncomeSerializer(ModelSerializer):
    class Meta:
        model = Income
        fields = ["id", "title", "description", "value", "updated_at", "category", "created_at"]
        read_only_fields = ["id", "updated_at"]
    def validate_category(self, value):
        if value not in INCOME_CHOICES_LIST:
            raise serializers.ValidationError(f"Категория '{value}' не является допустимой.")
        return value