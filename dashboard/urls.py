from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard_home'),
    path('inventory', views.inventory, name='dashboard_inventory'),
    path('login', views.login, name='login'),
]