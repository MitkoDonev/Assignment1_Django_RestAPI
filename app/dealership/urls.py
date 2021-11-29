from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import CarView, CarDetail, TruckView, TruckDetail

urlpatterns = [
    path('cars/', CarView.as_view()),
    path('cars/<int:pk>/', CarDetail.as_view()),
    path('trucks/', TruckView.as_view()),
    path('trucks/<int:pk>/', TruckDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
