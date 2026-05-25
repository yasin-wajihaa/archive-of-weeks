from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('on the courses yeah!')

