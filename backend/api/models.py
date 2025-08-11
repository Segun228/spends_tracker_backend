from django.db import models
from users.models import User


INCOME_CHOICES = [
    ("salary", "Зарплата"),
    ("freelance", "Дополнительный доход / Фриланс"),
    ("gift", "Подарки"),
    ("investment", "Инвестиции"),
    ("cashback", "Кэшбэк"),
    ("other", "Другое"),
]


EXPENSE_CHOICES = [
    ("rent", "Жилье / Аренда"),
    ("utilities", "Коммунальные платежи"),
    ("transport", "Транспорт"),
    ("communication", "Связь"),
    ("health", "Здоровье"),
    ("loan", "Кредиты"),
    ("groceries", "Продукты"),
    ("eating_out", "Кафе и рестораны"),
    ("clothes", "Одежда и обувь"),
    ("entertainment", "Развлечения"),
    ("gifts", "Подарки"),
    ("education", "Образование"),
    ("beauty", "Красота и уход"),
    ("other", "Другое"),
]

INCOME_CHOICES_LIST = [
    "salary",
    "freelance",
    "gift",
    "investment",
    "cashback",
    "other",
]


EXPENSE_CHOICES_LIST = [
    "rent",
    "utilities",
    "transport",
    "communication",
    "health",
    "loan",
    "groceries",
    "eating_out",
    "clothes",
    "entertainment",
    "gifts",
    "education",
    "beauty",
    "other",
]


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="spents")
    title = models.CharField(max_length=100, blank=True, default="")
    description = models.CharField(max_length=1000, blank=True, default="")
    value = models.IntegerField(default=0)
    category = models.CharField(        
        max_length=100,
        choices=EXPENSE_CHOICES,
        default="groceries",)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'

    def __str__(self):
        return self.title


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="incomes")
    title = models.CharField(max_length=100, blank=True, default="")
    description = models.CharField(max_length=1000, blank=True, default="")
    value = models.IntegerField(default=0)
    category = models.CharField(        
        max_length=100,
        choices=INCOME_CHOICES,
        default="groceries",)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'

    def __str__(self):
        return self.title



