from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

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
    "december":None
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys()) 
    return render(request,"challenges/index.html",{"months":months})

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
        raise Http404()
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
    