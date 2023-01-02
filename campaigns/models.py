from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta

# Create your models here.

class ContactPerson(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, blank=True)
    phone = models.CharField(max_length=12)
    


class Campaign(models.Model):
    action_types = [
        (1,"Informational campaign"),
        (2,"Politician reachout"),
        (3,"Neighbood event")
    ]
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    action_type = models.PositiveSmallIntegerField(choices = action_types, default = 1)
    short_description = models.TextField()
    long_description = models.TextField()
    due_date = models.DateField(default= date.today() + timedelta(days= 90))
    cover_image = models.ImageField(upload_to='images/', null=True, blank=True)
    completed_on = models.DateField(blank = True, null=True),
    completion_note = models.TextField(blank = True, null=True)
    url = models.URLField(max_length=200, blank=True)
    contact_person = models.ForeignKey(ContactPerson, on_delete=models.SET_DEFAULT, default=None, null=True)
    ready_for_release= models.BooleanField(default=False)
     
     
      
class CampaignUpdate(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=225)
    description = models.TextField()  
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, default=None, null = True )
    
class Action(models.Model):
    types = [
        (1,"Email"),
        (2,"Letter"),
        (3,"Tweet"),
        (4,"Instagram"),
        (5, 'Petitions'),
        (0,"Other"),      
    ]
    type = models.PositiveSmallIntegerField(choices = types, default = 1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=225)
    description = models.TextField()
    handle = models.CharField(max_length= 100)
    content = models.TextField()
    url = models.URLField(max_length=255, blank=True)
    file = models.FileField(upload_to ='actionfiles/', null=True, blank=True)
    active = models.BooleanField(default = False)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, default=None, null = True )