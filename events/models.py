from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db import models
import uuid
from users.models import Profile


# Create your models here.
class Events(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    description = models.TextField(max_length=1000)
    image = models.ImageField(null=True, blank=True, default='default.jpg')
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name




class User_Events(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=1000)
    image = models.ImageField(null=True, blank=True, default='default.jpg')
    time = models.TimeField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

