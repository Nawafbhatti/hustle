from django.shortcuts import render
from rest_framework import generics
from app.hustle_api.serializers import EventSerializer, GallerySerializer, ContactSerializer, CounterSerializer
from app.models import Event, Gallery, Contact, Items
from django.http import JsonResponse
from rest_framework.response import Response


# views start from here

class EventAPIView(generics.ListAPIView):
    
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class EventDetailAPI(generics.RetrieveAPIView):
    
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    lookup_field = 'slug'
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        
        sponsor_list = instance.get_sponsors_by_category()
        
        data = serializer.data
        data['sponsors'] = sponsor_list
        
        return Response(data)

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
        return Items.objects.filter(event=pk, use_in_home_page=False)
    

class HomeCounterAPI(generics.ListAPIView):
    
    serializer_class = CounterSerializer
    
    def get_queryset(self):
        return Items.objects.filter(use_in_home_page=True)