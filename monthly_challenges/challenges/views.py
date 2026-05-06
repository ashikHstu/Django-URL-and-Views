from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
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

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items+=f"<li><a href=\"{month_path}\">{capitalized_month} </a></li>"
    response_data =f"<ul>{list_items} </ul>"
    return HttpResponse(response_data)

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
        return render(request,"challenges/challenge.html", {
            "text":response,
            "title":"Monthly Challenge Test",
            "month": month
        })
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
    