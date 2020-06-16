from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'password')
        # Set custom ID and class for password field.
        widgets = {'password': forms.PasswordInput(attrs={'id': 'my_HTML_id', 'class':
                   'form-control','placeholder':'Password'}),
                   'username': forms.TextInput(attrs={'id': 'my_HTML_id', 'class':
                              'form-control','placeholder':'Username'})}
