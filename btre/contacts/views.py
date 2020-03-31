from django.shortcuts import render,redirect
from django.contrib import messages
from.models import Contacts
from django.core.mail import send_mail


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        id_user = request.POST['id_user']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            id_user = request.user.id
            has_contactred = Contacts.objects.all().filter(id_user=id_user,listing_id=listing_id)
            if has_contactred:
                messages.error(request,'You have alredy made')
                return redirect('listing')


        contact =Contacts(listing=listing,listing_id=listing_id,name=name,phone=phone,email=email,message=message,id_user=id_user,realtor_email=realtor_email)

        contact.save()
        send_mail('property','there aye','richard.black96@mail.ru',[realtor_email,'techgueinfo@mail.ru'],fail_silently=False)
        messages.success(request,'Yourrequest has beensubmited')
        return redirect('listings')
