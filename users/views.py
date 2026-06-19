from django.http import HttpResponse
from django.views.generic.edit import FormView
from .models import UserProfile
from django.db import transaction
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserRegisterForm
from django.contrib.auth.views import LoginView, LogoutView

def index(request):
    return HttpResponse('on the users yeah!')

class RegisterView(SuccessMessageMixin, FormView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = '/'
    success_message = 'User registered successfully!'

    @transaction.atomic
    def form_valid(self, form):
        user = form.save()
        pfp = form.cleaned_data['pfp']
        UserProfile.objects.create(pfp=pfp, user=user)

        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    next_page = '/'


class UserLogoutView(LogoutView):
    next_page = '/'


