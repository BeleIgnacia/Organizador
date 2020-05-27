from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('index/', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),

]
