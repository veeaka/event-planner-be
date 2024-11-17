import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from users.models import User
from events.models import Event
from datetime import datetime, timedelta


@pytest.fixture
def user(db):
    """Fixture for creating a test user."""
    return User.objects.create_user(
        email="testuser@example.com", password="testpassword"
    )


@pytest.fixture
def api_client(user):
    """Fixture for authenticated API client."""
    client = APIClient()
    client.force_authenticate(user=user)
    return client


@pytest.fixture
def past_event(user):
    """Fixture for creating a past event."""
    return Event.objects.create(
        user=user,
        title="Past Event",
        description="This is a past event.",
        date=datetime.now().date() - timedelta(days=2),
        time=(datetime.now() - timedelta(hours=2)).time(),
        location="Past Location",
    )


@pytest.fixture
def upcoming_event(user):
    """Fixture for creating an upcoming event."""
    return Event.objects.create(
        user=user,
        title="Upcoming Event",
        description="This is an upcoming event.",
        date=datetime.now().date() + timedelta(days=2),
        time=(datetime.now() + timedelta(hours=2)).time(),
        location="Upcoming Location",
    )


@pytest.mark.django_db
def test_create_event(api_client):
    """Test creating a new event."""
    url = reverse("event-list")
    data = {
        "title": "New Event",
        "description": "This is a new event.",
        "date": (datetime.now() + timedelta(days=1)).date().isoformat(),
        "time": (datetime.now() + timedelta(hours=1)).time().isoformat(),
        "location": "New Location",
    }
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Event.objects.count() == 1
    assert Event.objects.first().title == "New Event"


@pytest.mark.django_db
def test_retrieve_event(api_client, past_event):
    """Test retrieving an event."""
    url = reverse("event-detail", kwargs={"pk": past_event.id})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == past_event.title
    assert response.data["description"] == past_event.description
    assert response.data["location"] == past_event.location


@pytest.mark.django_db
def test_filter_past_events(api_client, past_event, upcoming_event):
    """Test filtering past events."""
    url = reverse("event-list")
    response = api_client.get(url, {"type": "past"})
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["title"] == past_event.title


@pytest.mark.django_db
def test_filter_upcoming_events(api_client, past_event, upcoming_event):
    """Test filtering upcoming events."""
    url = reverse("event-list")
    response = api_client.get(url, {"type": "upcoming"})
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["title"] == upcoming_event.title


@pytest.mark.django_db
def test_update_event(api_client, past_event):
    """Test updating an event."""
    url = reverse("event-detail", kwargs={"pk": past_event.id})
    data = {
        "title": "Updated Past Event",
        "description": "This is an updated past event.",
        "date": past_event.date.isoformat(),
        "time": past_event.time.isoformat(),
        "location": "Updated Location",
    }
    response = api_client.put(url, data)
    assert response.status_code == status.HTTP_200_OK
    past_event.refresh_from_db()
    assert past_event.title == "Updated Past Event"
    assert past_event.location == "Updated Location"


@pytest.mark.django_db
def test_partial_update_event(api_client, past_event):
    """Test partially updating an event."""
    url = reverse("event-detail", kwargs={"pk": past_event.id})
    data = {"title": "Partially Updated Title"}
    response = api_client.patch(url, data)
    assert response.status_code == status.HTTP_200_OK
    past_event.refresh_from_db()
    assert past_event.title == "Partially Updated Title"


@pytest.mark.django_db
def test_delete_event(api_client, past_event):
    """Test deleting an event."""
    url = reverse("event-detail", kwargs={"pk": past_event.id})
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Event.objects.count() == 0
