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

# Create your views here.
@login_required
def VisitLog(request,pk):
    form_cell = VisitForm()
    form_visitor = VisitorForm()
    form_cell.fields['location'].initial = pk
    location = Location.objects.get(pk=pk)
    visitors = Visitor.objects.all()
    return render(request,'home.html',{"form_cell":form_cell,"form_visitor":form_visitor,"location":location.name})

class VisitorListView(ListView,LoginRequiredMixin):
    model = Visitor

    def get_queryset(self):
        return Visitor.objects.order_by('name')

class VisitListView(ListView,LoginRequiredMixin):
    paginate_by = 2
    context_object_name = 'visit_list'
    queryset = Visit.objects.order_by('-timestamp')
    template_name='visit_list.html'

def postVisitor(request):
    # request should be ajax and method should be POST.
    form_cell = VisitForm()
    form_visitor = VisitorForm()
    response_data = {}
    if request.method == "POST":
        # get the form data
        cellphone = request.POST.get('cellphone')
        name = request.POST.get('name')
        location_id = request.POST.get('location')
        location = Location.objects.get(pk=location_id)
        temperature =request.POST.get('location')
        dry_cough = request.POST.get('location')
        breathing = request.POST.get('location')
        flu = request.POST.get('location'),
        other_contact = request.POST.get('location')
        # save the data and after fetch the object in instance
        if cellphone:
            #check if exists in database
            print(cellphone)
            if Visitor.objects.filter(cellphone=cellphone).exists():
                visitor = Visitor.objects.get(cellphone=cellphone)
                access_record= visitor.visit_set.create(location=location,
                                                        temperature=temperature,
                                                        dry_cough=dry_cough,
                                                        breathing= breathing,
                                                        flu= flu,
                                                        other_contact= other_contact)
                response_data['name'] = access_record.cellphone.name
                # ser_instance = serializers.serialize('json', [ instance, ])
                return JsonResponse(response_data)
            elif name:
                print(name)
                new_visitor=Visitor.objects.get_or_create(name=name,cellphone=cellphone)[0]
                new_visitor.save()
                print(new_visitor)
                access_record=new_visitor.visit_set.create(location=location,
                                                            temperature=temperature,
                                                            dry_cough=dry_cough,
                                                            breathing= breathing,
                                                            flu= flu,
                                                            other_contact= other_contact)
                print(access_record)
                response_data['name']=name
                # instance = new_visitor.name
                # ser_instance = serializers.serialize('json', [ instance, ])
                return JsonResponse(response_data)
            # instance = form.save()
            # # serialize in new friend object in json
            # ser_instance = serializers.serialize('json', [ instance, ])
            # # send to client side.
            # return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": cell.errors}, status=400)
    # some error occured
    return render(request,'home.html',{"form_cell":form_cell,"form_visitor":form_visitor})

def checkCell(request):
    # request should be ajax and method should be GET.
    if request.method == "GET":
        # get the nick name from the client side.
        cellphone = request.GET.get("cellphone", None)
        # check for the nick name in the database.
        if Visitor.objects.filter(cellphone = cellphone).exists():
            visitor = Visitor.objects.get(cellphone=cellphone)
            name = visitor.name
            # if nick_name found return not valid new friend
            return JsonResponse({"valid":False,"name":name}, status = 200)
        else:
            # if nick_name not found, then user can create a new friend.
            return JsonResponse({"valid":True}, status = 200)

    return JsonResponse({}, status = 400)

def Dashboard(request):
    return render(request,'dashboard.html')

def Tables(request):
    return render(request,'tables.html')







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
