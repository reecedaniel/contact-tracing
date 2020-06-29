from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView

class ThanksPage(TemplateView):
    template_name = 'thanks.html'


class index(TemplateView):
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("tracing:visits"))
        return super().get(request, *args, **kwargs)
