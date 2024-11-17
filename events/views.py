from rest_framework import viewsets
from .models import Event
from .serializers import EventDetailSerializer, EventCreateSerializer
from rest_framework.permissions import IsAuthenticated


from django.utils.timezone import now
from rest_framework import viewsets
from .models import Event
from .serializers import EventCreateSerializer, EventDetailSerializer
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return filtered queryset for past or upcoming events based on query parameters.
        """
        user_events = self.queryset.filter(user=self.request.user).order_by("-date")
        current_datetime = now()
        current_date = current_datetime.date()
        current_time = current_datetime.time()

        # Check for filtering based on 'type' query param
        event_type = self.request.query_params.get("type")
        if event_type == "past":
            return user_events.filter(
                Q(date__lt=current_date) | Q(date=current_date, time__lt=current_time)
            )
        elif event_type == "upcoming":
            return user_events.filter(
                Q(date__gt=current_date) | Q(date=current_date, time__gte=current_time)
            )

        # Default to all events for the user
        return user_events

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return EventCreateSerializer
        return EventDetailSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
