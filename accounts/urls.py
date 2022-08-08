from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product, name='products'),
    path('user/<str:pk>/', views.user, name='user'),
    path('create_sale/', views.createSale, name='create_sale'),
    path('update_sale/<str:pk>/', views.updateSale, name='update_sale'),
    path('delete_sale/<str:pk>/', views.deleteSale, name='delete_sale'),
]
