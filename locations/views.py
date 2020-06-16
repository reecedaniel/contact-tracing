from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,DetailView,UpdateView
from . import models
from braces.views import SelectRelatedMixin
from .forms import LocationUpdateForm
from tracing.filters import VisitFilter
# Create your views here.
class CreateLocation(LoginRequiredMixin,SelectRelatedMixin,CreateView):
    fields = ('name','address','city')
    model = models.Location

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class LocationList(LoginRequiredMixin,ListView):
    model = models.Location
    # select_related = ('user')

class LocationDetailView(UpdateView):
    context_object_name = 'location_detail'
    model = models.Location
    template_name = 'locations/location_detail.html'
    form_class=LocationUpdateForm

    def search(self,request,pk):
        location = Location.objects.get(pk=pk)
        visit_list = location.visit_set.all()
        visit_filter = VisitFilter(request.GET, queryset=visit_list)
        return render(request, 'locations/location_detail.html', {'filter': visit_filter})
    #automatically creates context dictionary school (i.e. model name in lower case)
