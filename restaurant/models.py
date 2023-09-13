from django.db import models
import uuid
from users.models import Profile
class Review(models.Model):
    by = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    project = models.ForeignKey('Restaurant', on_delete=models.CASCADE, null=True, blank=True)
    VOTE_TYPE = (
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    )
    title = models.CharField(max_length=100)
    body = models.TextField(null=True, blank=True)
    value = models.IntegerField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.title

class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=300)
    small_description = models.CharField(max_length=100, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    main_image = models.ImageField(null=True, blank=True, default='default.jpg')
    seats = models.IntegerField(default=0)
    open_from = models.TimeField(null=True, blank=True)
    open_to = models.TimeField(null=True, blank=True)
    large_description = models.TextField(max_length=1000, null=True, blank=True)

    # Facilities
    facilities = models.ManyToManyField('Facility', blank=True)

    # DaysOpen
    open_days = models.ManyToManyField('DayOpen')

    # Images
    images = models.ManyToManyField('Image', null=True, blank=True)

    def __str__(self):
        return self.name


class Facility(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class DayOpen(models.Model):
    DAYS = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )
    day = models.CharField(max_length=200, choices=DAYS)

    def __str__(self):
        return self.day


class Image(models.Model):
    image = models.ImageField(null=True, blank=True, default='default.jpg')

    def __str__(self):
        return self.image.url




