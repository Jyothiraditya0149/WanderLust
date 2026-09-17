# tours/admin.py
from django.contrib import admin
from .models import Tour, Booking, Review

# Register each model exactly ONCE
admin.site.register(Tour)
admin.site.register(Booking)
admin.site.register(Review)