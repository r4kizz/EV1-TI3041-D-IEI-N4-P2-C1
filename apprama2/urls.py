from django.urls import path
from . import views

urlpatterns = [
    path("v1/", views.vista1, name="vistarama1"),
    path("v2/", views.vista2, name="vistarama2"),
]