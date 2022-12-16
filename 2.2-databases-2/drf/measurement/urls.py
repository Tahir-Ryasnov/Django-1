from django.urls import path
from .views import ListView, SensorCreateAPIView, MeasurementCreateAPIView, UpdateAPIView
urlpatterns = [
    path('list/', ListView.as_view()),
    path('sensors/', SensorCreateAPIView.as_view()),
    path('measurements/', MeasurementCreateAPIView.as_view()),
    path('sensors/<pk>/', UpdateAPIView.as_view()),
]
