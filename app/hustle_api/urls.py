from django.urls import path
from app.hustle_api.views import EventAPIView, EventDetailAPI

urlpatterns = [
    path('', EventAPIView.as_view(), name="event-list"),
    path('event-detail/<int:pk>', EventDetailAPI.as_view(), name="event-detail"),
]