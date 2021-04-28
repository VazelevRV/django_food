from django.urls import path
from .views import reservations_view
urlpatterns = [
    path('view/', reservations_view),
]
