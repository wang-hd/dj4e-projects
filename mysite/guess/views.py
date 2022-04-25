from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def owner(request):
    return HttpResponse("Hello, world. 29579d09 is the polls index.")

def index(request):
    ans = """Add a number to the URL to guess the secret between 1 and 100\n
    like /guess/25"""
    return HttpResponse(ans)

def guess(request, guessvalue):
    ans = ""
    if guessvalue == 27 : ans = "Just right"
    elif guessvalue < 27 : ans = "Too low"
    else : ans = "Too high"

    resp = HttpResponse(ans)
    return resp