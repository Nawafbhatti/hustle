from rest_framework import serializers
from app.models import Event, Speaker, Sponsor, Gallery, Contact, SponsorCategory, Items, EventRegisterForm, PAYMENT

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
    
    class Meta:
        model = Event
        exclude= ('sponsors',)

class GallerySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Gallery
        fields = '__all__'
        
class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contact
        fields = '__all__'
        
class EventRegisterSerializer(serializers.ModelSerializer):
    
    event = EventSerializer(many=False, read_only=True)
    
    class Meta:
        model = EventRegisterForm
        fields = '__all__'
        
class PaymentSerializer(serializers.ModelSerializer):
    
    eventregister = EventRegisterSerializer(many=False, read_only=True)
    
    class Meta:
        model = PAYMENT
        fields = '__all__'