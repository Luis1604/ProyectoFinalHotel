from django.urls import path
from .views import index, registrar

urlpatterns = [
    path('', index),
    path('register/', registrar),
]
