# import form class from django
from django import forms

# import Student models from models.py
from .models import Student

# Django ModelForm - Create form from Models: Django ModelForm is a class that is used to directly convert a model into a Django form. 
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        #exclude =['roll_num']
