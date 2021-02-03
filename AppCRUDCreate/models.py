# import the standard Django Model 
# from built-in library
from django.db import models


# Create your models here.
# Declare a new model
class Student(models.Model):
    # Fields of the model
    fname = models.CharField(max_length=100, verbose_name='First name')
    lname = models.CharField(max_length=100, verbose_name='Last name')
    birthdate = models.DateField(verbose_name='Birthdate')
    subject = models.TextField(max_length=1000, verbose_name='Subject')
    roll_num = models.IntegerField()


    def __str__(self):
        return self.fname