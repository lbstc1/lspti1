from django.shortcuts import render
from django.http import *
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from.forms import *
from.models import *

def success(request):
    return render(request,'success.html')

def index(request):
    name=['comp','eng','math']
    name1 = ['comp1', 'eng1', 'math1']
    return render(request,'index.html',{'name':name,'name1':name1})

def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=UserCreationForm()
    return render(request,'register.html',{'form':form})

def StuReg_Form(request):
    form=StuRegForm
    if request.method=='POST':
        form=StuRegForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/StuReg_Form')
    else:
        return render(request,'Stu_Registration.html',{'form':form})

def All_Data(request):
    form=StuReg.objects.all()
    return render(request,'All_Data.html',{'form':form})


