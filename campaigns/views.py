from django.shortcuts import render
from django.http import HttpResponse
from .models import Campaign, ContactPerson

# Create your views here.
def index(request):
    campaign = Campaign.objects.filter(ready_for_release = True)
    print(campaign)
    
    context = {
        'campaigns': campaign
    }
    
    return render(request, 'home.html', context=context)

def showCampaignDetails(request, id):
    campaign = Campaign.objects.get(id = id)
    context = {
        'campaign': campaign
    }
    return render(request, 'campaingDetails.html', context = context)