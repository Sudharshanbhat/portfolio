from django.http import HttpResponse
from django.shortcuts import render

def cool_response(request):
    return render(request, "portfolio.html")