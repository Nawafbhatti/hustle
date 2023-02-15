from rest_framework import serializers
from app.models import Event, Speaker, Sponsor, Gallery, Contact, SponsorCategory, Items

class SponsorCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SponsorCategory
        fields = '__all__'

class SponsorSerializer(serializers.ModelSerializer):
    
    sponsor_type = SponsorCategorySerializer(many=False)
    class Meta:
        model = Sponsor
        fields = '__all__'

class SpeakerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Speaker
        fields = '__all__'

class CounterSerializer(serializers.ModelSerializer):
    Event = "EventSerializer(many=True)"
    
    class Meta:
        model = Items
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    
    speakers = SpeakerSerializer(many=True, read_only=True)
    sponsors = SponsorSerializer(many=True, read_only=True)
    
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