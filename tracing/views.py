from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from tracing.models import Visitor,Visit
from locations.models import Location
from tracing.forms import VisitorForm,VisitForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail,EmailMessage


# Create your views here.
@login_required
def VisitLog(request,pk):
    form_cell = VisitForm()
    form_visitor = VisitorForm()
    form_cell.fields['location'].initial = pk
    location = Location.objects.get(pk=pk)
    # visitors = Visitor.objects.all()

    return render(request,'home.html',{"form_cell":form_cell,"form_visitor":form_visitor,"location":location.name})

class VisitorListView(ListView,LoginRequiredMixin):
    model = Visitor

    def get_queryset(self):
        return Visitor.objects.order_by('name')

class VisitListView(ListView,LoginRequiredMixin):
    paginate_by = 10
    context_object_name = 'visit_list'
    queryset = Visit.objects.order_by('-timestamp')
    template_name='visit_list.html'

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
                new_visitor=Visitor.objects.get_or_create(name=name,cellphone=cellphone,email=v_email)[0]
                new_visitor.save()
                new_access_record=new_visitor.visit_set.create(location=location,
                                                            temperature=temperature,
                                                            dry_cough=dry_cough,
                                                            breathing= breathing,
                                                            flu= flu,
                                                            other_contact= other_contact)
                print("New Visitor Created")
                response_data['name']=name
                return JsonResponse(response_data)
        else:
            print("ERROR: FORM INVALID")
            return JsonResponse({"error": cell.errors}, status=400)
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
