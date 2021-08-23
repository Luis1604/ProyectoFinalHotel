from django.urls import path
from .views import login_view, inicio_view, reserva_view, servicio_view, registro_view
from django.urls.conf import include
from .views import personaViewSet, habitacionViewSet, reservaViewSet, registroHuespedesViewSet, serviciosViewSet
from rest_framework.routers import DefaultRouter, Route

router = DefaultRouter()
router.register('persona', personaViewSet, basename='persona')
router.register('habitacion', habitacionViewSet, basename='habitacion')
router.register('reservas', reservaViewSet, basename='reservas')
router.register('reshue', registroHuespedesViewSet, basename='reshue')
router.register('servicios', serviciosViewSet, basename='servicios')

urlpatterns = [
    path('', inicio_view, name='Login'),
    path('api/', include(router.urls)),
    path('home/', inicio_view),
    path('reserva/', reserva_view),
    path('servicios/', servicio_view),
    path('login/', login_view), 
    path('registro/', registro_view),
]
