from django.urls import path
from .views import sync_machine

urlpatterns = [
    path("sync/<str:serial_number>/", sync_machine, name="sync_machine"),
]