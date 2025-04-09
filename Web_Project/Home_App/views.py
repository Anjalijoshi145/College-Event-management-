from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages
from .models import*
from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm,EventForm,StudentForm
from .decorators import unauthenticated_user,allowed_users,admin_only
from django.shortcuts import get_object_or_404



# Create your views here.
@login_required(login_url='Login')
@admin_only
def dashboard(request):
    students=Student.objects.all()
    student=request.user.student
    event_registrations=User_Registration.objects.filter(name=student)
    event_register=User_Registration.objects.all()
    Events=Event.objects.all()
    total_events=Events.count()
    total_event_register=event_register.count()
    context={'students':students,'event_registrations':event_registrations,'event_register':event_register,'Events':Events,'total_events':total_events,'total_event_register':total_event_register}
    return render(request,'Dashboard/dashboard.html',context)

@login_required(login_url='Login')
def eventregister(request):
     if request.method =="POST":
        name=request.POST.get('name')
        course=request.POST.get('course')
        semester=request.POST.get('semester')
        event_name=request.POST.get('event_name')
        mobile_no= request.POST.get('mobile_no')
        email=request.POST.get('email')
        register=User_Registration(name=name,course=course,semester=semester,event_name=event_name, mobile_no=mobile_no,email=email, date=datetime.today())
        register.save()
        messages.success(request, 'Successfully Register for the event!')
     options=Event.objects.filter()
     context={'options':options}
     return render(request,'Main/eventregister.html',context)

@unauthenticated_user
def loginpage(request):
      if request.method=="POST":
          username=request.POST.get('username')
          password=request.POST.get('password')
          user=authenticate(request,username=username,password=password)
          if user is not None:
             login(request,user)
             if request.user.is_staff:
                return redirect('Dashboard')
             else:
                return redirect('userprofile')
          else:
             messages.error(request, 'Username or Password is incorrect')
      return render(request,'Main/login.html')


def home(request):
    events=Event.objects.all()
    return render(request,'Main/home.html',{'events':events})


def about(request):
    return render(request,'Main/about.html')


def event(request):
    events=Event.objects.all()
    return render(request,'Main/event.html',{'events':events})


def contact(request):
     if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact=Contact_Us(name=name,email=email,subject=subject,message=message,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
     return render(request,'Main/contact.html')

def logoutUser(request):
    logout(request)
    return redirect('Login')

@unauthenticated_user         
def register(request):
      form=CreateUserForm()
      if request.method=="POST":
         form=CreateUserForm(request.POST)
         if form.is_valid():
             user=form.save()
             username= form.cleaned_data.get('username')
             messages.success(request, 'Account has Successfully created for ' +  username)
             return redirect('Login')
         else:
            messages.error(request, ' Not Register Successfully!')

    
      context={'form':form}
      return render(request,'Main/register.html',context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin'])
def createEvents(request):
    form=EventForm()
    if request.method=="POST":
         form=EventForm(request.POST,request.FILES)
         if form.is_valid():
            form.save()
            return redirect('Dashboard')
    context={'form':form}
    return render(request,'Dashboard/event_form.html',context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin'])
def updateEvent(request,pk):
    events=Event.objects.get(id=pk)
    form=EventForm(instance=events)
    if request.method=="POST":
         form=EventForm(request.POST,request.FILES,instance=events)
         if form.is_valid():
            form.save()
            return redirect('Dashboard')
    context={'form':form}
    return render(request,'Dashboard/event_form.html',context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin'])
def deleteEvent(request,pk):
    events=Event.objects.get(id=pk)
    if request.method=='POST':
        events.delete()
        return redirect('Dashboard')
    context={'item':events}
    return render(request,'Dashboard/delete.html',context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['student'])
def UserProfile(request):
    student=request.user.student
    event_registrations_count=User_Registration.objects.filter(name=student).count()
    event_registrations=User_Registration.objects.filter(name=student)
    context={'student':student,'event_registrations_count':event_registrations_count,'event_registrations':event_registrations}
    return render(request,'Dashboard/user.html',context)


    
@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin'])
def student(request,student_id):
    student=get_object_or_404(Student,pk=student_id)
    event_registrations=User_Registration.objects.filter(name=student)
    event_registrations_count=User_Registration.objects.filter(name=student).count()
    context={'student':student,'event_registrations':event_registrations,'event_registrations_count':event_registrations_count}
    return render(request,'Dashboard/student.html',context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['student'])
def account_settings(request):
    student=request.user.student
    form=StudentForm(instance=student)
    if request.method=='POST':
        form=StudentForm(request.POST,request.FILES,instance=student)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'Dashboard/account_settings.html',context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin'])
def register_events(request):
    event_register=User_Registration.objects.all()
    context={'event_register':event_register}
    return render(request,'Dashboard/register_events.html',context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin'])
def contact_us(request):
    contacts=Contact_Us.objects.all()
    context={'contacts':contacts}
    return render(request,'Dashboard/contact_us.html',context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin'])
def Students_info(request):
    students=Student.objects.all()
    context={'students':students}
    return render(request,'Dashboard/Students.html',context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin'])
def deletestudent(request,student_id):
    student= get_object_or_404(Student,pk=student_id)
    if request.method=='POST':
        student.delete()
        return redirect('Dashboard')
    context={'student':student}
    return render(request,'Dashboard/delete_student.html',context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin'])
def deletecontact(request,contact_id):
    contact=get_object_or_404(Contact_Us,pk=contact_id)
    if request.method=='POST':
        contact.delete()
        return redirect('Dashboard')
    context={'contact':contact}
    return render(request,'Dashboard/delete_contact.html',context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin'])
def deleteregisterevent(request,event_id):
    events=get_object_or_404(User_Registration,pk=event_id)
    if request.method=='POST':
        events.delete()
        return redirect('Dashboard')
    context={'events':events}
    return render(request,'Dashboard/delete_register_event.html',context)