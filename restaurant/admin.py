from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Review, Restaurant, Facility, DayOpen, Image

admin.site.register(Review)  # Register an instance of the Review model
admin.site.register(Restaurant)
admin.site.register(Facility)
admin.site.register(DayOpen)
admin.site.register(Image)
