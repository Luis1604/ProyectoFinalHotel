from django.urls import path
from .views import index, registrar, login_view, inicio_view, reserva_view,servicio_view

urlpatterns = [
    path('', inicio_view,name='Login'),
    path('register/', registrar),
    path('reserva/', reserva_view),
    path('servicios/', servicio_view),
    path('login/', login_view),
]
