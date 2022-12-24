from django.shortcuts import render
from django.http import HttpResponse
from .models import Campaign, ContactPerson, CampaignUpdate, Action

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
    # campaignUpdates = campaign.campaignupdate_set().all()
    context = {
        'campaign': campaign,
        'updates':CampaignUpdate.objects.filter(campaign = campaign).order_by('-created_at'),
        'actions':Action.objects.filter(campaign = campaign).order_by('-type')
    }
    print("*******", CampaignUpdate.objects.filter(campaign = campaign))
    return render(request, 'campaingDetails.html', context = context)