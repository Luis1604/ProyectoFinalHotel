from django.urls import path
from .views import login_view, inicio_view, reserva_view, servicio_view, registrarList, registrarDetail
# registrar_list, registrar_detail

urlpatterns = [
    path('', inicio_view, name='Login'),
    #path('register/', registrar_list),
    #path('register/<int:pk>/', registrar_detail),
    path('register/', registrarList.as_view()),
    path('register/<int:pk>/', registrarDetail.as_view()),
    path('home/', inicio_view),
    path('reserva/', reserva_view),
    path('servicios/', servicio_view),
    path('login/', login_view),
]
