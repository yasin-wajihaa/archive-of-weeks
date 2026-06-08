from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from .models import UserProfile
from django.db import transaction


def index(request):
    return HttpResponse('on the users yeah!')

class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserCreationForm
    success_url = '/'

    @transaction.atomic
    def form_valid(self, form):
        user = form.save()
        UserProfile.objects.create(user=user)

        return super().form_valid(form)

