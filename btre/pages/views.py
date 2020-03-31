from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.chooices import bedroom_choices, price_choices, state_choices

def index(request):
    listings = Listing.objects.all().filter(is_published=True)[:3]
    return render(request,'pages/index.html',{'listings':listings,'state_choices':state_choices,'price_choices':price_choices,'bedroom_choices':bedroom_choices})

def about(request):
    realtors = Realtor.objects.all().filter(is_mvp=True)
    return render(request,'pages/about.html',{'realtors':realtors})
