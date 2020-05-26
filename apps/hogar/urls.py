from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('index/', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('services/', views.services, name='services'),
    path('shop/', views.shop, name='shop'),
    path('work_grid1/', views.work_grid1, name='work_grid1'),
    path('work_grid2/', views.work_grid2, name='work_grid2'),
    path('work/', views.work, name='work'),
    path('about/', views.about, name='about'),

 ]
