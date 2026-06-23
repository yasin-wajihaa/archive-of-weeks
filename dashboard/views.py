from django.shortcuts import render
from django.http import HttpResponse
from terms import utils


def dashboard(request):
    term = utils.current_term()
    year = utils.current_year()
    season = utils.current_season()
    today = utils.today()
    week = utils.current_week()
    week_remaining = 12-week
    active_courses_no = utils.active_courses().count()
    active_projects_no = utils.active_projects().count()
    active_courses = utils.active_courses()
    active_projects = utils.active_projects()

    return render(request, 'dashboard/home.html', {
        'term': term,
        'year': year,
        'season': season,
        'today_teehee': today,
        'week': week,
        'week_remaining': week_remaining,
        'active_projects_no': active_projects_no,
        'active_courses_no': active_courses_no,
        'active_projects': active_projects,
        'active_courses': active_courses

    })
