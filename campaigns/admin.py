from django.contrib import admin
from .models import Campaign, ContactPerson, CampaignUpdate
# Register your models here.
admin.site.register(ContactPerson)
admin.site.register(Campaign)
admin.site.register(CampaignUpdate)