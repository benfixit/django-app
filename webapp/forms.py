from django import forms
from .models import User
from django.core.validators import validate_email


class CreateUserForm(forms.ModelForm):
    min_name_length = 2

    class Meta:
        model = User
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(
                attrs={'id': 'name', 'class': 'form-control', 'required': True, 'min_length': 2, 'placeholder': 'Enter Name'}
            ),
            'email': forms.TextInput(
                attrs={'id': 'email', 'class': 'form-control', 'required': True, 'placeholder': 'Enter Email Address'}
            )
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            validate_email(email)
        except forms.ValidationError:
            raise forms.ValidationError("Please enter a valid email address!")
        return email

    def clean_name(self):
        name = self.cleaned_data.get('name')
        length_of_name = len(name)
        if length_of_name < self.min_name_length:
            raise forms.ValidationError("Name length is short!")
        return name
