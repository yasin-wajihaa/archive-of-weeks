from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from .models import UserProfile
from django.db import transaction
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

def index(request):
    return HttpResponse('on the users yeah!')

class RegisterView(SuccessMessageMixin, FormView):
    form_class = UserCreationForm
    template_name = 'users/register.html'
    success_url = '/'
    success_message = 'User registered successfully!'

    @transaction.atomic
    def form_valid(self, form):
        user = form.save()
        UserProfile.objects.create(user=user)

        return super().form_valid(form)

