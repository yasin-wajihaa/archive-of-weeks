from datetime import date
from .models import Term
from progress.models import Progress
from courses.models import Course, Project
from django.db.models import Max

def current_term():
    term = Term.objects.filter(start_date__lte=date.today(), end_date__gte=date.today()).first()
    return term

def current_year():
    return date.today().year

def today():
    return date.today()

def current_season():
    term = current_term()
    t = str(term)[-1]
    season_name = None
    if t == '1':
        season_name = 'Spring'
    elif t == '2':
        season_name = 'Summer'
    else:
        season_name = 'Fall'
    return season_name

def current_week():
    week = Progress.objects.aggregate(Max("week")) or 1
    return week['week__max']

def active_courses():
    term = current_term()
    active= Course.objects.filter(term=term)
    return active

def active_projects():
    term = current_term()
    active = Project.objects.filter(term=term)
    return active