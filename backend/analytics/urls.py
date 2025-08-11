from django.urls import path, include
from .views import StatsView

urlpatterns = [
    path("stats/", StatsView.as_view(), name="expenses-static-endpoint"),
]