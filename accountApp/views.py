from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Account


# Create your views here.

# default function
def index(request):
    allPeople = Account.objects.all()
    context = {
        'allPeople': allPeople
    }
    return render(request, "accountApp/index.html", context)

# Function that's print The person name we write on the input field
def welcomePerson(request):
    print(request.POST)
    return HttpResponse("Welcome to the "+request.POST["personName"]+"'s account")

# Function that add $5 on each person's checking account
def addAmount(request, personID):
    everyOne = get_object_or_404(Account, pk=personID)
    everyOne.checking += 5
    everyOne.save()
    return redirect("index")

# Challenge
def amountAdded(request):
    return HttpResponse(request.POST["amountToAdd"])