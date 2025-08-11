from django.urls import path, include
from .views import StatsView, VisualView

urlpatterns = [
    path("stats/", StatsView.as_view(), name="expenses-static-endpoint"),
    path("visual/", VisualView.as_view(), name="expenses-static-endpoint"),
]