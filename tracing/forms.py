from django import forms
from tracing.models import Visitor,Visit


class VisitorForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)

    def __init__(self, *args, **kwargs):
        super(VisitorForm, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
        })


class VisitForm(forms.Form):
    cellphone = forms.CharField(label='Cellphone', max_length=10,widget=forms.NumberInput)
    location = forms.CharField(label='Location',max_length=200)

    def __init__(self, *args, **kwargs):
        super(VisitForm, self).__init__(*args, **kwargs)
        self.fields["location"] = forms.CharField(widget=forms.HiddenInput())
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
