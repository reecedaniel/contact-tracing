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
        self.object = self.get_object(queryset=models.Location.objects.all())
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
        unique_visits = month_visits.values('cellphone').annotate(cell_count=Count('cellphone')).order_by().filter(cell_count__gt=1)
        context['unique'] = unique_visits.count()

        # repeats = visits_data.annotate(num_visits=Count('timestamp'))
        # print(repeats[0].num_visits)
        # context['repeats_today'] = repeats.filter(timestamp__gt = today).count()
        return context

    def get_queryset(self):
        return self.object.visit_set.all().order_by('-timestamp')

    # def def render_to_json_response(self, context, **response_kwargs):
    #     """
    #     Returns a JSON response, transforming 'context' to make the payload.
    #     """
    #     return JsonResponse(
    #         self.get_data(context),
    #         **response_kwargs
    #     )
