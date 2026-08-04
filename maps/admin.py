from django.contrib import admin
from .models import Location, TouristAttraction, EVChargingStation, Route, Waypoint


# ===========================
# Location Admin
# ===========================
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location_type",
        "address",
        "is_active",
        "created_at",
    )

    list_filter = (
        "location_type",
        "is_active",
        "created_at",
    )

    search_fields = (
        "name",
        "description",
        "address",
    )

    list_editable = (
        "is_active",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        ("Basic Information", {
            "fields": (
                "name",
                "description",
                "location_type",
            )
        }),
        ("Coordinates", {
            "fields": (
                "latitude",
                "longitude",
                "address",
            )
        }),
        ("Status", {
            "fields": (
                "is_active",
                "created_at",
                "updated_at",
            )
        }),
    )


# ===========================
# Tourist Attraction Admin
# ===========================
@admin.register(TouristAttraction)
class TouristAttractionAdmin(admin.ModelAdmin):

    list_display = (
        "location",
        "category",
        "rating",
        "entry_fee",
    )

    list_filter = (
        "category",
    )

    search_fields = (
        "location__name",
        "location__address",
    )

    autocomplete_fields = (
        "location",
    )

    fieldsets = (
        ("Location", {
            "fields": (
                "location",
            )
        }),
        ("Attraction Details", {
            "fields": (
                "category",
                "rating",
                "entry_fee",
                "opening_time",
                "closing_time",
                "contact_number",
                "website",
                "image",
            )
        }),
    )


# ===========================
# EV Charging Station Admin
# ===========================
@admin.register(EVChargingStation)
class EVChargingStationAdmin(admin.ModelAdmin):

    list_display = (
        "location",
        "charger_type",
        "power_level",
        "number_of_ports",
        "is_operational",
    )

    list_filter = (
        "charger_type",
        "power_level",
        "is_operational",
    )

    search_fields = (
        "location__name",
        "location__address",
        "operator",
    )

    autocomplete_fields = (
        "location",
    )

    fieldsets = (
        ("Location", {
            "fields": (
                "location",
            )
        }),
        ("Station Details", {
            "fields": (
                "operator",
                "charger_type",
                "power_level",
                "number_of_ports",
                "charging_speed",
                "cost_per_kwh",
            )
        }),
        ("Availability", {
            "fields": (
                "is_operational",
                "available_24_7",
                "requires_membership",
                "contact_number",
            )
        }),
    )


# ===========================
# Waypoint Inline
# ===========================
class WaypointInline(admin.TabularInline):
    model = Waypoint
    extra = 0
    fields = (
        "name",
        "latitude",
        "longitude",
        "order",
    )


# ===========================
# Route Admin
# ===========================
@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "start_location",
        "end_location",
        "total_distance",
        "estimated_time",
        "created_at",
    )

    list_filter = (
        "created_at",
    )

    search_fields = (
        "name",
        "start_location__name",
        "end_location__name",
        "created_by",
    )

    readonly_fields = (
        "created_at",
    )

    autocomplete_fields = (
        "start_location",
        "end_location",
    )

    inlines = [
        WaypointInline,
    ]

    fieldsets = (
        ("Route Information", {
            "fields": (
                "name",
                "created_by",
            )
        }),
        ("Locations", {
            "fields": (
                "start_location",
                "end_location",
            )
        }),
        ("Metrics", {
            "fields": (
                "total_distance",
                "estimated_time",
                "path_coordinates",
            )
        }),
        ("Metadata", {
            "fields": (
                "created_at",
            )
        }),
    )