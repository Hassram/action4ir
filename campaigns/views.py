from django.shortcuts import render
from django.http import HttpResponse
from .models import Campaign, ContactPerson

# Create your views here.
def index(request):
    campaign = Campaign.objects.all()
    print(campaign)
    
    context = {
        'campaigns': campaign
    }
    
    return render(request, 'home.html', context=context)