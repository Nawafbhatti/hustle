from django.shortcuts import render
from rest_framework import generics
from app.hustle_api.serializers import EventSerializer
from app.models import Event

class EventAPIView(generics.ListAPIView):
    
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    
class EventDetailAPI(generics.RetrieveAPIView):
    
    serializer_class = EventSerializer
    queryset = Event.objects.all()