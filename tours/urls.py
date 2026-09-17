# tours/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # 1. HOME PAGE (The missing link!)
    path('', views.home, name='home'),

    # 2. TOUR LIST
    path('tours/', views.tour_list, name='tour_list'),

    # 3. TOUR DETAIL
    path('tour/<int:pk>/', views.tour_detail_and_book, name='tour_detail'),

    # 4. SIGNUP
    path('signup/', views.SignUpView.as_view(), name='signup'), 

    # 5. ADD REVIEW (The new feature)
    path('tour/<int:pk>/review/', views.add_review, name='add_review'),
]