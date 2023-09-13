from django.contrib import admin

# Register your models here.
from .models import Events,User_Events
admin.site.register(Events)
admin.site.register(User_Events)