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

# BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
class VisitForm(forms.Form):
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

    cellphone = forms.CharField(label='Cellphone', max_length=10,widget=forms.NumberInput)
    location = forms.CharField(label='Location',max_length=200)
    temperature = forms.DecimalField(max_digits=3,decimal_places=1)
    dry_cough = forms.ChoiceField(choices = BOOL_CHOICES, label="Do you have a dry cough?",
                              initial='False', widget=forms.Select(attrs={'class':'custom-toggle-slider rounded-circle'}), required=True)
    breathing = forms.ChoiceField(choices = BOOL_CHOICES, label="Do you have difficulty breathing?",
                              initial='False', widget=forms.Select(), required=True)
    flu=forms.ChoiceField(choices = BOOL_CHOICES, label="Do you have flu symptoms?",
                              initial='False', widget=forms.Select(), required=True)
    other_contact=forms.ChoiceField(choices = BOOL_CHOICES, label="Have you been in contact with anyone with flu-like symptoms?",
                              initial='False', widget=forms.Select(), required=True)


    def __init__(self, *args, **kwargs):
        super(VisitForm, self).__init__(*args, **kwargs)
        self.fields["location"] = forms.CharField(widget=forms.HiddenInput())
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
