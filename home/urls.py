from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.index, name="home"), #for subcribe button
    path("about", views.about, name="About"),
    path("product", views.product, name="product"),
    path("contact", views.contact, name="contact"), 
]