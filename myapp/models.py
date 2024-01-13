from django.db import models
# models.py
from django.contrib.auth.models import User
from django.db.models import JSONField
import uuid




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.CharField(max_length=200, null=True)
    zipCode = models.IntegerField()
    countryCode = models.CharField(max_length=120, null=True)
    mobile = models.CharField(max_length=120, unique=True)
    picture = models.URLField(max_length=255, blank=True, null=True)
    # walking = models.CharField(max_length=200,blank=True,)
    # running = models.CharField(max_length=200,blank=True,)
    # gardening = models.CharField(max_length=200,blank=True, null=True)
    # swimming = models.CharField(max_length=200,blank=True,null=True)
    # coffeeTea = models.CharField(max_length=200,blank=True, null=True)
    # foodGathering = models.CharField(max_length=200,blank=True, null=True)
    # televisionSports = models.CharField(max_length=200,blank=True, null=True)
    # movies = models.CharField(max_length=200,blank=True, null=True)
    # shopping = models.CharField(max_length=200,blank=True, null=True)
    # happyHours = models.CharField(max_length=200,blank=True, null=True)
    # errands = JSONField(blank=True, null=True)
    # rides = models.CharField(max_length=200,blank=True, null=True)
    # childcare = models.CharField(max_length=200,blank=True, null=True)
    # eldercare = models.CharField(max_length=200,blank=True, null=True)
    # petcare = models.CharField(max_length=200,blank=True, null=True)
    # tutoring = models.CharField(max_length=200,blank=True, null=True)
    # repairAdvice = models.CharField(max_length=200,blank=True, null=True)
    # otherAdvice = models.CharField(max_length=200,blank=True, null=True)
    
    walking = JSONField(blank=True, null=True)
    running = JSONField(blank=True, null=True)
    dog = JSONField(blank=True, null=True)
    gardening = JSONField(blank=True, null=True)
    swimming = JSONField(blank=True, null=True)
    coffeeTea = JSONField(blank=True, null=True)
    art = JSONField(blank=True, null=True)
    foodGathering = JSONField(blank=True, null=True)
    sports = JSONField(blank=True, null=True)
    movies = JSONField(blank=True, null=True)
    shopping = JSONField(blank=True, null=True)
    happyHours = JSONField(blank=True, null=True)
    rides = JSONField(blank=True, null=True)
    childcare = JSONField(blank=True, null=True)
    eldercare = JSONField(blank=True, null=True)
    petcare = JSONField(blank=True, null=True)
    repairAdvice = JSONField(blank=True, null=True)
    tutoring = JSONField(blank=True, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    sharePreference = models.CharField(max_length=200, null=True)
    email_confirmed = models.BooleanField(default=False)
    interests_updated = models.BooleanField(default=False)
    confirmation_token = models.UUIDField(default=uuid.uuid4, editable=False)

def __str__(self):
        return self.user.username

# Create your models here.
