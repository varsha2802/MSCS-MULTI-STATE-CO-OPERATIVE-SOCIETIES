import os
import tempfile
from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from home.models import Registration
from home.models import GraphData
from home.models import Grievance
from home.models import Feedback
from django.core.files import File
from django.conf import settings

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from tkinter import Tk
import matplotlib
matplotlib.use('Agg')

from django.contrib import messages

# Create your views here.
def index(request):
    context={
        'variable': "varsha"
        #models ki value fetch krke bhej skte hai
    }
    
    return render(request,'index.html',context)

def homelogout(request):
    if request.user.is_anonymous:
        return render(request,'index.html')
    return render(request,'userfiles/index.html')


def mscsform(request):
     return render(request,'base-form.html')

def formlogout(request):
    return render(request,'userfiles/base-form.html')



def formi(request):
    return render(request,'form-i.html')

def formilogout(request):
    return render(request,'userfiles/form-i.html')



def formii(request):
    return render(request,'form-ii.html')

def formiilogout(request):
    return render(request,'userfiles/form-ii.html')



def formiii(request):
    return render(request,'form-iii.html')

def formiiilogout(request):
    return render(request,'userfiles/form-iii.html')



def formiv(request):
    return render(request,'form-iv.html')

def formivlogout(request):
    return render(request,'userfiles/form-iv.html')


def formv(request):
    return render(request,'form-v.html')

def formvlogout(request):
    return render(request,'userfiles/form-v.html')



def mscslogin(request):
    return render(request,'base-login.html')

def mscsloginlogout(request):
    return render(request,'userfiles/base-login.html')



def mscsact(request):
    return render(request,'base-mscsact.html')

def mscsactlogout(request):
    return render(request,'userfiles/base-mscsact.html')


def adminlogin(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            fname=user.first_name
            messages.success(request,"Successfully logged in!")
            return redirect('homelogout')

        else:
            messages.error(request,"Wrong password or username, Please Try Again!")
            return redirect('adminlogin')



    return render(request,'admin-login.html')

# def loginuser(request):
#     if request.method=='POST':
#         username= request.POST.get('username')
#         password= request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request,user)
#             return redirect("/homelogout")
#         else:
#             return render(request,'index.html')




def checklist(request):
    return render(request,'checklist.html')

def checklistlogout(request):
    return render(request,'userfiles/checklist.html')


def modelbye(request):
    return render(request,'modelbye.html')

def modelbyelogout(request):
    return render(request,'userfiles/modelbye.html')

def logoutuser(request):
    logout(request)
    return redirect("home")

def regS(request):
    return render(request,'basic-regs.html')


def regSlogout(request):
    return render(request,'userfiles/basic-regs.html')


def chartslogout(request):
    return render(request,'userfiles/base-chart.html')
   
# def chart1logout(request):
#     return render(request,'userfiles/chart1.html')

def chart1logout(request):
    return render(request,'userfiles/chart1.html')

def chart1(request):
    return render(request,'chart1.html')

def chart2(request):
    return render(request,'chart2.html')

def chart3(request):
    return render(request,'chart3.html')

def chart2logout(request):
    return render(request,'userfiles/chart2.html')

def chart3logout(request):
    return render(request,'userfiles/chart3.html')

def form(request):
    return render(request,'registration.html')

def contact(request):
    return render(request,'contact_us.html')

def contactlogout(request):
    return render(request,'userfiles/contact_us.html')



def grievanceform(request):
    return render(request,'form-2.html')

def feedbackform(request):
    return render(request,'form-3.html')

def feedbackformlogout(request):
    return render(request,'userfiles/form-3.html')

def feedback2(request):
    # date=datetime.today()
    if request.method == "POST":
       
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        typeoffeedback = request.POST.get('typeoffeedback')
        
        address=request.POST.get('address')
        subject=request.POST.get('subject')
        file=request.FILES.get('file')
        

        fed=Feedback(name=name, email=email, mobile=mobile,typeoffeedback=typeoffeedback,address=address,subject=subject,file=file,date=datetime.today())
        fed.save()
        
        messages.success(request,"Feedback Registered!")
    return redirect('feedbackformlogout')

def feedback(request):
    # date=datetime.today()
    if request.method == "POST":
       
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        typeoffeedback = request.POST.get('typeoffeedback')
        
        address=request.POST.get('address')
        subject=request.POST.get('subject')
        file=request.FILES.get('file')
        

        fed=Feedback(name=name, email=email, mobile=mobile,typeoffeedback=typeoffeedback,address=address,subject=subject,file=file,date=datetime.today())
        fed.save()
        
        messages.success(request,"Feedback Registered!")
    return redirect('feedbackform')


def grievanceformlogout(request):
    return render(request,'userfiles/form-2.html')


def grievance(request):
    if request.method == "POST":
       
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        mobile = request.POST.get('mobile')
        email = request.POST.get('email')

        typeofcomplaint= request.POST.get('typeofcomplaint')
        societycomplaint = request.POST.get('societycomplaint')
        complaint = request.POST.get('complaint')

        gre=Grievance(fname=fname, lname=lname,email=email, mobile=mobile,typeofcomplaint=typeofcomplaint,societycomplaint=societycomplaint, complaint=complaint,date=datetime.today())
        gre.save()
        
        messages.success(request,"Grievance Registered!")
    return redirect('grievanceform')

def grievance2(request):
    if request.method == "POST":
       
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        mobile = request.POST.get('mobile')
        email = request.POST.get('email')

        typeofcomplaint= request.POST.get('typeofcomplaint')
        societycomplaint = request.POST.get('societycomplaint')
        complaint = request.POST.get('complaint')

        gre=Grievance(fname=fname, lname=lname,email=email, mobile=mobile,typeofcomplaint=typeofcomplaint,societycomplaint=societycomplaint, complaint=complaint,date=datetime.today())
        gre.save()
        
        messages.success(request,"Grievance Registered!")
    return redirect('grievanceformlogout')



def registration(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        desig = request.POST.get('desig')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')

        country= request.POST.get('country')
        state = request.POST.get('state')
        district = request.POST.get('district')
        
        md = request.POST.get('md')
        address = request.POST.get('address')

        pan = request.POST.get('pan')
        tan = request.POST.get('tan')
        service = request.POST.get('service')

        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

       



        if User.objects.filter(username=username):
            messages.error(request,"Username already exists, please try some other username")
            return redirect('form')

        if User.objects.filter(email=email):
            messages.error(request,"Email already registered")
            return redirect('form')
        
        if len(username)>20:
            messages.error(request, "username must be under 20 characters")
            return redirect('form')


        if not username.isalnum():
            messages.error(request, "username must be Alpha-Numeric")
            return redirect(form)

        if password!=confirm:
            messages.error(request,"Passwords didn't match! Please Try Again!")
            return redirect('form')

        reg=Registration(username=username, fname=fname, lname=lname, desig=desig, email=email, mobile=mobile, country=country, state=state, district=district, address=address, md=md, pan=pan, tan=tan, service=service, password=password, confirm=confirm, date=datetime.today())
        reg.save()
        
        myuser= User.objects.create_user(username,email,password)
        myuser.first_name=fname
        myuser.last_name=lname
             
        myuser.save()
        messages.success(request,"You are Registered!")
    return redirect('adminlogin')


def statewise(request):
    return render(request, 'state.html')
def statewiselogout(request):
    return render(request, 'userfiles/state.html')

def registrars(request):
    return render(request,'registrars.html')
def registrarslogout(request):
    return render(request,'userfiles/registrars.html')

def related(request):
    return render(request,'related.html')

def relatedlogout(request):
    return render(request,'userfiles/related.html')

def societies(request):
    return render(request,'societies.html')

def societieslogout(request):
    return render(request,'userfiles/societies.html')

def disclaimer(request):
    return render(request,'disclaimer.html')
def disclaimerlogout(request):
    return render(request,'userfiles/disclaimer.html')
