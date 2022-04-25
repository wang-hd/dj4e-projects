from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def owner(request):
    return HttpResponse("Hello, world. 29579d09 is the polls index.")

def myview(request):
    count = request.session.get('count', 0) + 1
    request.session['count'] = count
    if count > 5 : del(request.session['count'])
    resp = HttpResponse("view count=" + str(count))
    resp.set_cookie('dj4e_cookie', '29579d09', max_age=1000)
    return resp
