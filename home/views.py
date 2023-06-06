from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import contacts
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'sample1-home.html')

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is about")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("This is services")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = contacts(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
    #return HttpResponse("This is contact")

