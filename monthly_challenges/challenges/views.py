from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    return HttpResponse("This works!")

monthly_challenges = {
    "january":"January clicked",
    "february":"February clicked",
    "march":"March clicked",
    "april":"April clicked",
    "may":"May clicked",
    "june":"June clicked",
    "july":"July licked",
    "august":"August clicked",
    "september":"September clicked",
    "october":"October clicked",
    "november":"November clicked",
    "december":"December clicked"
}

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month>len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge",args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request,month):
    try:
        response = monthly_challenges[month]
        return HttpResponse(response)
    except:
        return HttpResponseNotFound("This month is not supported!")
    

