from django.urls import path
from apps.interfaz.views import Home

urlpatterns = [
    path('', Home.as_view()),
]