from django.shortcuts import render,get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
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
    model = User
    context_object_name = "subscriber"

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs.get('username'))

    # def get_context_data(self, **kwargs):
        # context = super(UserSubscription,self).get_context_data(**kwargs)
        # context['subscriber'] = self.get_object()
        # context['locations_used'] = self.get_object().location_set.count()


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
