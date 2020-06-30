from django.shortcuts import render,get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth import get_user_model
from accounts.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,DetailView
from . import forms
from .models import Profile
from locations.models import Location
from braces.views import SelectRelatedMixin

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"

class UserSubscription(LoginRequiredMixin,DetailView):
    model = get_user_model()
    context_object_name = "subscriber"

    def get_object(self):
        return get_object_or_404(User, email=self.kwargs.get('email'))
