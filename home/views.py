from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import contacts
from django.contrib import messages
#email subscribe files
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import SubscribedUsers
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
    if request.method == 'POST':  #for subcribe newsletter
        email = request.POST.get('email', None)

        if not email:
            messages.error(request, "You must type legit email to subscribe to a Newsletter")
            return redirect("/")

        if get_user_model().objects.filter(email=email).first():
            messages.error(request, f"Found registered user with associated {email} email. You must login to subscribe or unsubscribe.")
            return redirect(request.META.get("HTTP_REFERER", "/")) 

        subscribe_user = SubscribedUsers.objects.filter(email=email).first()
        if subscribe_user:
            messages.error(request, f"{email} email address is already subscriber.")
            return redirect(request.META.get("HTTP_REFERER", "/"))  

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")

        subscribe_model_instance = SubscribedUsers()
        subscribe_model_instance.email = email
        subscribe_model_instance.save()
        messages.success(request, f'{email} email was successfully subscribed to our newsletter!')
        return render(request, 'sample1-home.html')
        
    return render(request, 'sample1-home.html')
    
def about(request):
    return render(request, 'about.html')
    

def product(request):
    return render(request, 'product.html')
    #return HttpResponse("This is servicess")

def contact(request):
    if request.method == "POST":   #for conatcts save
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = contacts(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent! We will in touch with you')
    return render(request, 'contact.html')
    #return HttpResponse("This is contact")

