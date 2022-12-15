from django.contrib import admin
from .models import Campaign, ContactPerson
# Register your models here.
admin.site.register(ContactPerson)
admin.site.register(Campaign)