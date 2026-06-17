from django.urls import path
from .views import home, about, vehicles, vehicle_detail, parts, sold_vehicles
urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('vehicles/', vehicles, name='vehicles'),
    path('vehicle/<int:vehicle_id>/', vehicle_detail, name='vehicle_detail'),
    path('parts/', parts, name='parts'),
    path('sold-vehicles/', sold_vehicles, name='sold_vehicles'),
]