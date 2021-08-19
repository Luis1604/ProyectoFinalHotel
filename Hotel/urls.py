from django.urls import path
from .views import index, registrar_list, registrar_detail, login_view, create_view, inicio_view, reserva_view

urlpatterns = [
    path('', login_view, name='Login'),
    path('register/', registrar_list),
    path('register/<int:pk>/', registrar_detail),
    path('create/', create_view),
    path('home/', inicio_view),
    path('reserva/', reserva_view),
]
