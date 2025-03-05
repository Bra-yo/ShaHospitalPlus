from django.shortcuts import render,redirect,get_object_or_404
from HospitalApp.models import *

# Create your views here.
def services(request):
    return render(request, 'services.html')

def starter(request):
    return render(request, 'starter-page.html')

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'About.html')

def departments(request):
    return render(request, 'departments.html')

def doctors(request):
    return render(request, 'doctors.html')

def contact(request):
    if request.method == "POST":
        contactus = Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        contactus.save()
        return redirect('/contact')
    else:
        return render(request, 'contact.html')


def appoint(request):
    if request.method=="POST":
       myappointments = Appointment(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            date = request.POST['date'],
            department = request.POST['department'],
            doctor = request.POST['doctor'],
            message = request.POST['message'],
        )
       myappointments.save()
       return redirect('/show')
    else:
        return render(request, 'Appointment.html')


def show(request):
    All = Appointment.objects.all()
    return render(request, 'show.html',{'appnts':All})

def delete(request,id):
    deleteappointment= Appointment.objects.get(id=id)
    deleteappointment.delete()
    return redirect('/show')


def cnts(request):
    conts = Contact.objects.all()
    return render(request, 'allcontacts.html',{'conts':conts})

def delcont(request,id):
    deletecontact= Contact.objects.get(id=id)
    deletecontact.delete()
    return redirect('/all contacts')

def edit(request,id):
    editappointment= get_object_or_404(Appointment,id=id)
    if request.method == 'POST':
        editappointment.name = request.POST.get('name')
        editappointment.email = request.POST.get('email')
        editappointment.phone = request.POST.get('phone')
        editappointment.date = request.POST.get('date')
        editappointment.department = request.POST.get('department')
        editappointment.doctor = request.POST.get('doctor')
        editappointment.message = request.POST.get('message')
        editappointment.save()
        return redirect('/show')
    else:
        return render(request,'edit.html',{'editappointment':editappointment})

def register(request):
    return render (request,'Register.html')


def login_view(request):
    return render (request,'login.html')