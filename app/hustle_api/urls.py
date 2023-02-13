from django.urls import path
from app.hustle_api.views import EventAPIView, EventDetailAPI, GalleryListView, Contact_create 

urlpatterns = [
    path('', EventAPIView.as_view(), name="event-list"),
    path('gallery-list/', GalleryListView.as_view(), name="gallery-list"),
    path('create-contact/', Contact_create.as_view(), name="create-contact"),
    
    path('event-detail/<int:pk>', EventDetailAPI.as_view(), name="event-detail"),
]