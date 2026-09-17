# tours/forms.py
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        # Fields that the user will input:
        fields = ['customer_name', 'customer_email', 'customer_phone', 'number_of_people']
        # Optional: Customize field labels
        labels = {
            'customer_name': 'Your Full Name',
            'customer_email': 'Your Email Address',
            'customer_phone': 'Phone Number (Optional)',
            'number_of_people': 'Number of Travelers',
        }
        # Optional: Set widget attributes (like min value for a number input)
        widgets = {
            'number_of_people': forms.NumberInput(attrs={'min': 1, 'max': 10}),
        }
    # tours/forms.py
from django import forms
from .models import Booking, Review

# ... (Keep BookingForm here) ...

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        labels = {
            'rating': 'Rating (1-5 Stars)',
            'comment': 'Write your review',
        }
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5, 'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }