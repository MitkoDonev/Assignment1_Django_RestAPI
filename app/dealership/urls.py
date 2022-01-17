from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, TruckViewSet

router = DefaultRouter()

router.register(r"cars", CarViewSet, basename="car")
router.register(r"trucks", TruckViewSet, basename="truck")
urlpatterns = router.urls
