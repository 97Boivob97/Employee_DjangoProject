from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'address', 'phone_number', 'salary', 'designation', 'short_description']

    address = forms.CharField(widget=forms.TextInput)
    short_description = forms.CharField(widget=forms.TextInput)