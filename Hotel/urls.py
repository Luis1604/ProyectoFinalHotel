from django.urls import path
from .views import index, registrar, login_view, create_view, inicio_view, reserva_view

urlpatterns = [
    path('', login_view,name='Login'),
    path('register/', registrar),
    path('create/', create_view),
    path('home/', inicio_view),
    path('reserva/', reserva_view),
]
