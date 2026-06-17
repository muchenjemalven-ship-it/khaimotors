from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from core.views import (
    home,
    about,
    vehicles,
    vehicle_detail,
    parts,
    sold_vehicles
)

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('vehicles/', vehicles, name='vehicles'),
    path('vehicle/<int:vehicle_id>/', vehicle_detail, name='vehicle_detail'),
    path('parts/', parts, name='parts'),
    path('sold-vehicles/', sold_vehicles, name='sold_vehicles'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)