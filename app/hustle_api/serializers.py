from rest_framework import serializers
from app.models import Event, Speaker, Sponsor, Gallery, Contact


class SponsorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sponsor

class SpeakerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Speaker

class EventSerializer(serializers.ModelSerializer):
    
    sponsor = serializers.StringRelatedField(many=True, read_only=True)
    speaker = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Event
        fields = '__all__'

class GallerySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Gallery
        fields = '__all__'
        
class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contact
        fields = '__all__'