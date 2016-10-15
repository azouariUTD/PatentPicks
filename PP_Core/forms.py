from django import forms
from .models import User

class RegisterForm(forms.Form):
    first_name = forms.CharField(label="first_name", required=True)
    last_name = forms.CharField(label="last_name", required=True)
    email = forms.CharField(label="email", required=True)
    password = forms.CharField(label="password", required=True)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()

        # get form values
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

