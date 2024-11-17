from rest_framework import serializers
from .models import Event


class EventCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ["id", "title", "description", "date", "time", "location"]


class EventDetailSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()
    time = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "description",
            "date",
            "time",
            "location",
        ]

    def get_date(self, obj):
        # Format date as '11 Nov'
        return obj.date.strftime("%d %b %y")

    def get_time(self, obj):
        # Format time as '11:20 AM' or '11:20 PM'
        return obj.time.strftime("%I:%M %p")
