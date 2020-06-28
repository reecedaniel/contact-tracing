from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from tracing.models import Visitor,Visit
from locations.models import Location
from tracing.forms import VisitorForm,VisitForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse,HttpResponseBadRequest
from django.urls import reverse
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail,EmailMessage
from django.contrib import messages
import datetime
from django.db.models import Min, Max, Sum


# Create your views here.
@login_required
def VisitLog(request,pk):
    form_cell = VisitForm()
    form_visitor = VisitorForm()
    form_cell.fields['location'].initial = pk
    location = Location.objects.get(pk=pk)
    # visitors = Visitor.objects.all()

    return render(request,'home.html',{"form_cell":form_cell,"form_visitor":form_visitor,"location":location.name})

#notbeingused
class VisitorListView(LoginRequiredMixin,ListView):
    model = Visitor

    def get_queryset(self):
        return Visitor.objects.filter(user=self.request.user).order_by('name')

class VisitListView(LoginRequiredMixin,ListView):
    # paginate_by = 10
    context_object_name = 'visit_list'
    # queryset = Visit.objects.select_related('location__user').filter(location__user=self.request.user).order_by('-timestamp')
    template_name='visit_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.date.today()
        month = today.month
        day= today.day
        all_visits = self.get_queryset()
        month_visits = all_visits.filter(timestamp__month = month)
        last_month_visits = all_visits.filter(timestamp__month = month-1)
        high_temp_today = all_visits.filter(timestamp__day = day,temperature__gte=38)
        context['month_visits'] = month_visits.count()
        context['last_month_visits'] = last_month_visits.count()
        context['today_visits'] = all_visits.filter(timestamp__day = day).count()
        print(all_visits.filter(timestamp__day = day-1).count())
        context['yesterday_visits']= all_visits.filter(timestamp__day = day-1).count()
        context['average_per_day']= self.average_visits_per_day()
        context['high_temp_today']= high_temp_today.count()

        return context

    def get_queryset(self): #should probably include this in models as a manager
        queryset = Visit.objects.select_related('location__user').filter(location__user=self.request.user).order_by('-timestamp')
        return queryset

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

def checkCell(request):
    # request should be ajax and method should be GET.
    if request.method == "GET":
        # get the nick name from the client side.
        cellphone = request.GET.get("cellphone", None)
        # check for the nick name in the database.
        if Visitor.objects.filter(cellphone = cellphone).exists():
            visitor = Visitor.objects.get(cellphone=cellphone)
            name = visitor.name
            v_email = visitor.visitor_email
            # if nick_name found return not valid new friend
            return JsonResponse({"valid":False,"name":name,"email":v_email}, status = 200)
        else:
            # if nick_name not found, then user can create a new friend.
            return JsonResponse({"valid":True}, status = 200)

    return JsonResponse({}, status = 400)

def Dashboard(request):
    return render(request,'dashboard.html')

def Tables(request):
    return render(request,'tables.html')


def formSubmit(request):
    form_cell = VisitForm()
    form_visitor = VisitorForm()
    response_data = {}
    if request.method == 'POST':
        access_record = VisitForm(request.POST)
        visitor = VisitorForm(request.POST)
        if access_record.is_valid() & visitor.is_valid():
            cellphone = access_record.cleaned_data['cellphone']
            location_id = access_record.cleaned_data['location']
            location = Location.objects.get(pk=location_id)
            print(location)
            temperature = access_record.cleaned_data['temperature']
            dry_cough = access_record.cleaned_data['dry_cough']
            breathing = access_record.cleaned_data['breathing']
            flu = access_record.cleaned_data['flu']
            other_contact = access_record.cleaned_data['other_contact']
            name = visitor.cleaned_data['name']
            v_email = visitor.cleaned_data['visitor_email']

            if Visitor.objects.filter(cellphone=cellphone).exists():
                existing_visitor = Visitor.objects.get(cellphone=cellphone)
                new_access_record= existing_visitor.visit_set.create(location=location,
                                                        temperature=temperature,
                                                        dry_cough=dry_cough,
                                                        breathing= breathing,
                                                        flu = flu,
                                                        other_contact= other_contact)
                print("New record for existing visitor")
                response_data['name'] = new_access_record.cellphone.name
            else:
                new_visitor=Visitor.objects.get_or_create(name=name,cellphone=cellphone,visitor_email=v_email)[0]
                new_visitor.save()
                new_access_record=new_visitor.visit_set.create(location=location,
                                                            temperature=temperature,
                                                            dry_cough=dry_cough,
                                                            breathing= breathing,
                                                            flu= flu,
                                                            other_contact= other_contact)
                print("New Visitor Created")
                response_data['name']=name
            response_data['message'] = "Visit Logged"
            return JsonResponse(response_data)
        else:
            print("ERROR: FORM INVALID")
            # errors = access_record.errors.as_JSON()
            return JsonResponse({"error": access_record.errors}, status=400)
    return render(request,'home.html',{"form_cell":form_cell,"form_visitor":form_visitor})


# class CreateVistorView(CreateView):
#     redirect_field_name = 'home.html'
#     form_class = VisitorForm
#     model = Visitor
#
# class CreateVisitView(CreateView):
#     redirect_field_name = 'home.html'
#     form_class = VisitForm
#     model = Visit


# def visit(request):
#
#     if request.method == "POST":
#         access_form = VisitForm(data=request.POST)
#         visitor_form = VisitorForm(data=request.POST)
#
#         if access_form.is_valid():
#             accessed = access_form.save(commit=False)
#             if Visitor.filter(cellphone=accessed.cellphone).exists():
#                 accessed.save()
#             elif visitor_form.is_valid():
#                 new_visitor = visitor_form.save()
#                 accessed.cellphone=new_visitor.cellphone
#                 accessed.save()
#             else:
#                 print(visitor_form.errors)
#         else:
#             print(access_form.errors)
#     else:
#         access_form = VisitForm()
#         visitor_form = VisitorForm()
#
#     return render(request,'home.html',{'access_form':access_form,
#                                                 'visitor_form':visitor_form})
