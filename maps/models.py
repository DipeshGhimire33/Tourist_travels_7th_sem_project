
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Location(models.Model):

    LOCATION_TYPES = [
        ('general', 'General'),
        ('attraction', 'Tourist Attraction'),
        ('charging', 'EV Charging Station'),
    ]

    location_type = models.CharField(
        max_length=20,
        choices=LOCATION_TYPES,
        default='general'
    )

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    latitude = models.FloatField(
        validators=[MinValueValidator(-90), MaxValueValidator(90)]
    )

    longitude = models.FloatField(
        validators=[MinValueValidator(-180), MaxValueValidator(180)]
    )

    address = models.CharField(max_length=500, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class TouristAttraction(models.Model):
    location = models.OneToOneField(
        Location,
        on_delete=models.CASCADE,
        related_name="tourist_attraction"
    )

    CATEGORY_CHOICES = [
            ('historical', 'Historical Site'),
            ('natural', 'Natural Wonder'),
            ('museum', 'Museum'),
            ('religious', 'Religious Site'),
            ('entertainment', 'Entertainment'),
            ('adventure', 'Adventure Activity'),
            ('cultural', 'Cultural Site'),
            ('beach', 'Beach'),
            ('park', 'Park/Garden'),
            ('viewpoint', 'Viewpoint'),
            ('other', 'Other'),
        ]

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        null=True,
        blank=True
    )

    entry_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    opening_time = models.TimeField(null=True, blank=True)
    closing_time = models.TimeField(null=True, blank=True)

    contact_number = models.CharField(max_length=20, blank=True)
    website = models.URLField(blank=True)

    image = models.ImageField(
        upload_to="attractions/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.location.name


class EVChargingStation(models.Model):

    location = models.OneToOneField(
        Location,
        on_delete=models.CASCADE,
        related_name="charging_station"
    )

    CHARGER_TYPE_CHOICES = [
            ('type1', 'Type 1 (J1772)'),
            ('type2', 'Type 2 (Mennekes)'),
            ('ccs', 'CCS (Combined Charging System)'),
            ('chademo', 'CHAdeMO'),
            ('tesla', 'Tesla Supercharger'),
            ('universal', 'Universal'),
        ]
        
    POWER_LEVEL_CHOICES = [
            ('level1', 'Level 1 (120V)'),
            ('level2', 'Level 2 (240V)'),
            ('dcfast', 'DC Fast Charging'),
        ]
    

    charger_type = models.CharField(
        max_length=20,
        choices=CHARGER_TYPE_CHOICES
    )

    power_level = models.CharField(
        max_length=20,
        choices=POWER_LEVEL_CHOICES
    )

    number_of_ports = models.PositiveIntegerField(default=1)

    charging_speed = models.CharField(max_length=50)

    is_operational = models.BooleanField(default=True)

    cost_per_kwh = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )

    operator = models.CharField(max_length=100, blank=True)

    available_24_7 = models.BooleanField(default=False)

    requires_membership = models.BooleanField(default=False)

    def __str__(self):
        return self.location.name

 

class Route(models.Model):
    name = models.CharField(max_length=200)

    start_location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name="routes_from"
    )

    end_location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name="routes_to"
    )

    total_distance = models.FloatField()

    estimated_time = models.FloatField(
        null=True,
        blank=True
    )

    path_coordinates = models.JSONField(default=list)

    created_at = models.DateTimeField(auto_now_add=True)
    
class Waypoint(models.Model):
    """
    Model for intermediate points/stops in a route.
    Each waypoint belongs to a specific route and has an order.
    """
    route = models.ForeignKey(
        Route, 
        on_delete=models.CASCADE, 
        related_name='waypoints'
    )
    name = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    order = models.PositiveIntegerField(
        help_text="Order of this waypoint in the route (1, 2, 3, ...)"
    )
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.name} (Stop {self.order})"
