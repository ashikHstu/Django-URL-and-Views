from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("This works!")


def monthly_challenge(request,month):
    response = "Not supported."
    if month=="January":
        response = "Januray clicked"
    elif month == "February":
        response = "February clicked"
    return HttpResponse(response)

