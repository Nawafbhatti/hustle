from rest_framework import serializers
from app.models import Event, Speaker, Sponsor


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
        exclude = ['id']