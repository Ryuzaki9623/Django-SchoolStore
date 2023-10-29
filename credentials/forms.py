from django import forms
from .models import Department,Course,Purpose
class RegistrationForm(forms.Form):
    
    name = forms.CharField(label="Name", required=True)
    dob = forms.DateField(label="Date of Birth", required=True)
    age = forms.IntegerField(label="Age", required=True)
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = forms.ChoiceField(label="Gender", choices=GENDER_CHOICES, widget=forms.RadioSelect, required=True)
    phone = forms.CharField(label="Phone Number", required=True, widget=forms.TextInput(attrs={'type': 'tel'}))
    email = forms.EmailField(label="Email Address", required=True)
    address = forms.CharField(label="Address", widget=forms.Textarea(attrs={'rows': 4}), required=True)
    department = forms.ModelChoiceField(queryset=Department.objects.all(), empty_label=None)
    course = forms.ModelChoiceField(queryset=Course.objects.all(), empty_label=None)
    purpose = forms.ChoiceField(choices=Purpose.PURPOSE_CHOICES)

    materials = forms.MultipleChoiceField(
        label="Materials Provided",
        choices=[
            ('Notebook', 'Notebook'),
            ('Pen', 'Pen'),
            ('Exam Papers', 'Exam Papers'),
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
