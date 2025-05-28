from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('vehicules/', views.car_list, name='car_list'),
    path('appartements/', views.apartment_list, name='apartment_list'),
    path('vehicule/<int:id>/', views.car_detail, name='car_detail'),
    path('appartement/<int:id>/', views.apartment_detail, name='apartment_detail'),
    path('reserver/', views.reserve_both, name='reserve_both'),  # Nouvelle ligne
    path('reserver-combine/', views.reserve_both, name='reserve_both'),
]