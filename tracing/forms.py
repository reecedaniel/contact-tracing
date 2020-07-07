from django import forms
from tracing.models import Visitor,Visit
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Field


class VisitorForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    visitor_email = forms.EmailField(label='Email',max_length=254)

    def __init__(self, *args, **kwargs):
        super(VisitorForm, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
        })


class ToggleWidget(forms.widgets.CheckboxInput):
    template_name = 'toggle.html'

    # def __init__(self, attrs=None, *args, **kwargs):
    #     attrs = attrs or {}
    #
    #     default_options = {
    #         'on': 'Yes',
    #         'off': 'No'
    #     }
    #     options = kwargs.get('options', {})
    #     default_options.update(options)
    #     for key, val in default_options.items():
    #         attrs['data-' + key] = val
    #
    #     super().__init__(attrs)

class VisitForm(forms.Form):
    # BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
    cellphone = forms.CharField(label='Cellphone',min_length=10,max_length=10,widget=forms.NumberInput)
    location = forms.CharField(label='Location',max_length=200,widget=forms.HiddenInput())
    temperature = forms.DecimalField(max_digits=3,decimal_places=1)
    dry_cough = forms.BooleanField(label="Do you have a dry cough?",required=False,widget=ToggleWidget)
    breathing = forms.BooleanField(label="Do you have difficulty breathing?",required=False,widget=ToggleWidget)
    flu=forms.BooleanField(label="Do you have flu symptoms?",required=False,widget=ToggleWidget)
    other_contact=forms.BooleanField(label="Have you been in contact with anyone with flu-like symptoms?",required=False,widget=ToggleWidget)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper(self)
    #     # self.helper.form_class = 'form-group'
    #     self.helper.layout = Layout(
    #         Field('cellphone', css_class='form-control'),
    #         Field('temperature', css_class='form-control'),
    #         CustomCheckbox('dry_cough'),
    #         CustomCheckbox('breathing'),
    #         CustomCheckbox('flu'),
    #         CustomCheckbox('other_contact'),
    #     )
        # super(VisitForm, self).__init__(*args, **kwargs)
        # self.fields["location"] = forms.CharField(widget=forms.HiddenInput())
        # ## add a "form-control" class to each form input
        # ## for enabling bootstrap
        # for name in self.fields.keys():
        #     self.fields[name].widget.attrs.update({
        #         'class': 'form-control',
        #     })
