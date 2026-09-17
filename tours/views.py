# tours/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Tour, Booking, Review
from .forms import BookingForm, ReviewForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Avg


def home(request):
    return render(request, 'home.html')

def tour_list(request):
    available_tours = Tour.objects.filter(is_available=True)
    return render(request, 'tours/tour_list.html', {'tours': available_tours})

# 3. TOUR DETAIL & BOOKING VIEW
def tour_detail_and_book(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    
    # Calculate Average Rating
    avg_rating = tour.reviews.aggregate(Avg('rating'))['rating__avg'] or 0

    if request.method == 'POST':
        # If we are here, it MUST be the booking form, because the review form 
        # posts to a different URL ('add_review')
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.tour = tour
            booking.save()
            messages.success(request, f"🎉 Booking confirmed for {tour.title}!")
            return redirect('tour_list')
    else:
        booking_form = BookingForm()

    # Review form is always blank here
    review_form = ReviewForm()

    context = {
        'tour': tour,
        'form': booking_form,
        'review_form': review_form,
        'reviews': tour.reviews.all().order_by('-created_at'),
        'avg_rating': round(avg_rating, 1),
    }
    return render(request, 'tours/tour_detail.html', context)

# 4. ADD REVIEW VIEW
def add_review(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.tour = tour
            review.user = request.user
            review.save()
            messages.success(request, "Thank you! Your review has been posted.")
    return redirect('tour_detail', pk=pk)

# 5. SIGNUP VIEW
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'