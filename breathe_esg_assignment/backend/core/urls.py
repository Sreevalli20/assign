from django.urls import path
from ingestion.views import upload_data, records

urlpatterns = [
    path('api/upload/', upload_data),
    path('api/records/', records),
]