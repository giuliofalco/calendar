from django.contrib import admin
from django.urls import path, include  # Importa include per collegare le URL dell'app

urlpatterns = [
    path('admin/', admin.site.urls),  # URL per il pannello di amministrazione
    path('', include('cal.urls')),   # Include le URL dell'app 'cal' per la root
]

