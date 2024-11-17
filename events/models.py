from django.db import models

from django.conf import settings

User = settings.AUTH_USER_MODEL


class BaseModal(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Event(BaseModal):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, help_text="User who created this event"
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(help_text="Date of the event")
    time = models.TimeField(help_text="Time of the event")
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title
