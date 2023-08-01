from django import forms
from crudProject1.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'email']