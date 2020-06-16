from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView
from . import forms
from . import models
from braces.views import SelectRelatedMixin

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"

# class CreateLocation(LoginRequiredMixin,SelectRelatedMixin,CreateView):
#     fields = ('name','address','city')
#     model = models.Location
#
#     def form_valid(self,form):
#         self.object = form.save(commit=False)
#         self.object.user = self.request.user
#         self.object.save()
#         return super().form_valid(form)
#
# class LocationList(LoginRequiredMixin,ListView):
#     model = models.Location
#     # select_related = ('user')
