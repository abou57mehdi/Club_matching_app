from django.urls import path

from .views import club_matching_view

urlpatterns = [
    path('', club_matching_view, name='club_matching'),
    # Add other app-specific URL patterns here
]
