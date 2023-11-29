from django import forms
from .models import Student

class DateInput(forms.DateInput):
    input_type = 'date'
# class Materials(forms.ModelForm):
#     materials=forms.BooleanField()
#
#     def __init__(self):
#         if check_something():
#             self.fields['materials'].initial = True
#
#     class meta:
#         model=Student
#         fields=['materials']
#         labels={'materials':'pen'}

class Studentform(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets={
            'Dob':DateInput(),
        }