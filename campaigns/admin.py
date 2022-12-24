from django.contrib import admin
from .models import Campaign, ContactPerson, CampaignUpdate, Action
# Register your models here.
admin.site.register(ContactPerson)
admin.site.register(Campaign)
admin.site.register(CampaignUpdate)
admin.site.register(Action)