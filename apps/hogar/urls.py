from django.urls import path

from apps.hogar.views import dashboard

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
]