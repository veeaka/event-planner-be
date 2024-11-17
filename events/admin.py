from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "date", "time", "location")
    search_fields = ("title", "description", "location")
    list_filter = ("date", "time")
    ordering = ("date", "time")
    date_hierarchy = "date"

    # Optional: Customizing the form display
    fieldsets = (
        (None, {"fields": ("user", "title", "description")}),
        (
            "Event Details",
            {
                "fields": ("date", "time", "location"),
                "classes": ("collapse",),
            },
        ),
    )


admin.site.register(Event, EventAdmin)
