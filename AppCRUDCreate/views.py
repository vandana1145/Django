from django.shortcuts import render
from .forms import StudentForm
from .models import Student
from django.http import HttpResponse

# Create your views here.
def createStudent(req):
    form = StudentForm()
    # if req.method == 'POST':
    #     form = StudentForm(req.POST)
    #     if form.is_valid():
    #         try:
    #             form.save()
    #             return redirect('/create')
    #         except:
    #             pass
    #     else:
    #         form = StudentForm()

    return render(req, 'createStudent.html', {'form':form})


    
