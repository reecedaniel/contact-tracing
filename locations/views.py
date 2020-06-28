from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,DetailView,UpdateView
from django.views.generic.detail import SingleObjectMixin
from . import models
from braces.views import SelectRelatedMixin
from .forms import LocationUpdateForm, LocationCreateForm
from django.contrib.messages.views import SuccessMessageMixin
from tracing.models import Visit
from django.http import JsonResponse
import datetime
from django.db.models import Count
from django.db.models import Min, Max, Sum

# Create your views here.
class CreateLocation(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    template_name = 'locations/location_form.html'
    form_class = LocationCreateForm
    # success_message = 'Success: Location was created.'
    # success_url = reverse_lazy('locations:locations')

    def form_valid(self,form):
        self.save_user(form)
        return super(CreateLocation,self).form_valid(form)

    def save_user(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

class LocationUpdate(LoginRequiredMixin,UpdateView):
    context_object_name = 'location_detail'
    model = models.Location
    template_name = 'locations/location_form.html'
    form_class=LocationUpdateForm

    def get_context_data(self, **kwargs):
        loc = self.get_object()
        context = super().get_context_data(**kwargs)
        context['location_pk'] = loc.pk
        print('context: ', context)
        return context

    # def dispatch(self, *args, **kwargs):
    #     self.location_id = kwargs['pk']
    #     return super(LocationUpdateView, self).dispatch(*args, **kwargs)


class LocationList(LoginRequiredMixin,ListView):
    model = models.Location
    # select_related = ('user')

#TO DELETE
class LocationDetailView(LoginRequiredMixin,UpdateView):
    context_object_name = 'location_detail'
    model = models.Location
    template_name = 'locations/location_detail.html'
    form_class=LocationUpdateForm

    #automatically creates context dictionary school (i.e. model name in lower case)

class LocationDetail(LoginRequiredMixin,SingleObjectMixin,ListView):
    template_name = 'locations/location_detail2.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=models.Location.objects.filter(user=self.request.user))
        # queryset = self.get_queryset()
        # data = list(queryset.values())
        # return JsonResponse(data, safe=False)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['location'] = self.object
        visits_data = self.get_queryset()
        context['total_visits'] = visits_data.count()
        today = datetime.date.today()
        month = today.month
        month_visits = visits_data.filter(timestamp__month = month)
        context['month'] = month_visits.count()
        unique_visits = month_visits.values('cellphone').annotate(cell_count=Count('cellphone')).order_by().filter(cell_count__gt=0)
        context['unique'] = unique_visits.count()
        context['average_per_day']= self.average_visits_per_day()

        return context

    def get_queryset(self):
        return self.object.visit_set.all().order_by('-timestamp')

    def average_visits_per_day(self):
        aggregate = self.get_queryset().aggregate(Min('timestamp'), Max('timestamp'))
        min_datetime = aggregate.get('timestamp__min')
        if min_datetime is not None:
            min_date = min_datetime.date()
            max_date = aggregate.get('timestamp__max').date()
            total_visits = self.get_queryset().count()
            days = (max_date - min_date).days + 1
            return round(total_visits / days)
        return 0
