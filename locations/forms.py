from django import forms
from locations.models import Location

class LocationUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LocationUpdateForm, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
        })


    class Meta:
        model = Location
        fields = ('name','address','city')
        # Set custom ID and class for password field.
        # widgets = {'password': forms.PasswordInput(attrs={'id': 'my_HTML_id', 'class':
        #            'form-control','placeholder':'Password'}),
        #            'username': forms.TextInput(attrs={'id': 'my_HTML_id', 'class':
        #                       'form-control','placeholder':'Username'})}
