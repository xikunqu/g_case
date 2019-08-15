from django.urls import path,include
from backend.views import add_data


urlpatterns = [
    path('data/',add_data),
]
