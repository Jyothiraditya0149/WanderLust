
from django.db import models

class Tour(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.IntegerField()
    is_available = models.BooleanField(default=True)
    
    image = models.ImageField(upload_to='tour_images/', blank=True, null=True)

    def __str__(self):
        return self.title

class Booking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20, blank=True, null=True) 
    booking_date = models.DateTimeField(auto_now_add=True)
    number_of_people = models.IntegerField(default=1)

    def __str__(self):
        return f"Booking for {self.tour.title} by {self.customer_name}"
    
from django.db import models
from django.contrib.auth.models import User  # Import User model
from django.core.validators import MinValueValidator, MaxValueValidator # Limits for 1-5 stars


class Review(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.tour.title} ({self.rating}★)"