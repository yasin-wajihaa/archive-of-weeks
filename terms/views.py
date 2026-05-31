from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse('Everything you want in gold<br>'
                        'I\'ll be the magic story you\'ve told!' )
