from django.contrib import admin
from home.models import contacts
from home.models import SubscribedUsers

# Register your models here.
admin.site.register(contacts)
admin.site.register(SubscribedUsers)