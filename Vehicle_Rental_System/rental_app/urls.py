from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vehicles/', views.vehicle_list, name='vehicle-list'),
    path('vehicles/<slug:slug>/', views.vehicle_list_filtered, name='vehicle-list-filtered'),
    path('vehicle/<int:pk>/', views.vehicle_detail, name='vehicle-detail'),
    path('vehicle/<int:pk>/rent/', views.rent_vehicle, name='rent-vehicle'),
    path('checkout/', views.checkout, name='checkout'),
    path('confirm/', views.confirm_rental, name='confirm-rental'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
