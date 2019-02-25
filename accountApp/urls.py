from django.urls import path
from . import views

# URLs
urlpatterns = [
    path("", views.index, name="index"),
    path("welcomePerson/", views.welcomePerson, name="welcomePerson"),
    path("addAmount/<int:personID>/", views.addAmount, name="addAmount"),
    # Challenge
    path("amountAdded/<int:amountID>/", views.amountAdded, name="amountAdded"),
]