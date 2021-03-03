from django.http import  HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from.forms import StudentForm
from .models import Student

def index(request):
    students = Student.get_all()  #通过Student模型拿到所有的student数据，然后放到context传递到模板
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentForm()

    context = {
        'students': students,
        'form': form,

    }
    return render(request,'index.html', context=context) #render做成映射
# Create your views here.
