from django.shortcuts import render,get_object_or_404
from.models import Listing
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from .chooices import bedroom_choices, price_choices, state_choices

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    #Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    #City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
    #state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)
    #bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
    #price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    return render(request,'listings/search.html',{'listings':queryset_list,'values':request.GET,'state_choices':state_choices,'price_choices':price_choices,'bedroom_choices':bedroom_choices})

def listings(request):
    listings = Listing.objects.all().filter(is_published=True)
    paginator = Paginator(listings,1)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    return render(request,'listings/listings.html',{'listings':paged_listings})

def listing(request,id):
    listing = get_object_or_404(Listing,id=id)
    return render(request,'listings/listing.html',{'listing':listing})
