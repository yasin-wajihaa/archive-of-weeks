from django.shortcuts import render
from django.http import HttpResponse
from terms import utils


def home(request):
    term = utils.current_term()
    year = utils.current_year()
    season = utils.current_season()
    today = utils.today()
    week = utils.current_week()
    week_remaining = 12-week

    return render(request, 'dashboard/home.html', {
        'term': term,
        'year': year,
        'season': season,
        'today_teehee': today,
        'week': week,
        'week_remaining': week_remaining,

    })
