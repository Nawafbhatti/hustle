from django.shortcuts import render
from rest_framework import generics
from app.hustle_api.serializers import EventSerializer, GallerySerializer, ContactSerializer, CounterSerializer
from app.models import Event, Gallery, Contact, Items

class EventAPIView(generics.ListAPIView):
    
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    
class EventDetailAPI(generics.RetrieveAPIView):
    
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    
class GalleryListView(generics.ListAPIView):
    
    serializer_class = GallerySerializer
    queryset = Gallery.objects.all()
    
class Contact_create(generics.CreateAPIView):
    
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    
class CounterItemAPI(generics.ListAPIView):
    
    serializer_class = CounterSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Items.objects.filter(event=pk)