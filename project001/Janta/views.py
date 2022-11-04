from ast import Or
from multiprocessing import context, managers
from unicodedata import name
from urllib import response
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .filter import *
from django.http import HttpResponse
import csv
from datetime import datetime
import smtplib
from django.contrib.auth.decorators import login_required
from .decorators import admin_only
# from djqscsv import render_to_csv_response

# Create your views here.
@login_required(login_url='login')
def jantadashboard(request):
    managers = Manager.objects.all()
    total_managers = Manager.objects.count()

    writers = Writer.objects.all()
    total_writers = Writer.objects.count()

    total_orders = Order.objects.count()

    context = {'managers':managers, 'total_managers':total_managers, 'writers':writers, 'total_writers':total_writers,
    'total_orders':total_orders}
    return render(request, 'admin/dashboard.html', context)

def managerlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            messages.warning(request, f"Username or Password does not exist")

    context = {}
    return render(request, 'janta/login.html', context)

def managerlogout(request):
    logout(request)
    return redirect('/')

def managerprofile(request):
    manager = request.user.manager
    form = AddManagerForm(instance=manager)

    if request.method == 'POST':
        form = AddManagerForm(request.post, request.FILES, instance=manager)
        if form.is_valid():   
            form.save()

    context = {'form':form}
    return render(request, 'janta/managerprofile.html', context)

@login_required(login_url='login')
def managerdashboard(request):
    writers = Writer.objects.all()
    total_writers = Writer.objects.count()
    total_orders = Order.objects.count()

    orders = Order.objects.all()

    context = {'writers':writers, 'total_writers':total_writers, 'total_orders':total_orders, 'orders':orders}
    return render(request, 'janta/managerdashboard.html', context)

@login_required(login_url='login')
def addorder(request):
    form = AddOrderForm()
    if request.method == 'POST':
        form = AddOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
    
    writers = Writer.objects.all()

    context = {'form':form, 'writers':writers}
    return render(request, 'janta/addorder.html', context)

@login_required(login_url='login')
def editorder(request,pk):
    order = Order.objects.get(id=pk)
    form = AddOrderForm(instance=order)
    if request.method == 'POST':
        form = AddOrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
    
    writers = Writer.objects.all()

    context = {'form':form, 'writers':writers}
    return render(request, 'janta/editorder.html', context)

@login_required(login_url='login')
def deleteorder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/dashboard')

    context = {'order':order}
    return render(request, 'janta/deleteorder.html', context)

@login_required(login_url='login')
def createmanager(request):
    form = AddManagerForm()
    if request.method == 'POST':
        form = AddManagerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/jantaadmin')

    context = {'form':form}
    return render(request, 'Janta/createmanager.html', context)

@login_required(login_url='login')
def updatemanager(request, pk):
    manager = Manager.objects.get(id=pk)
    form = AddManagerForm(instance=manager)
    if request.method == 'POST':
        form = AddManagerForm(request.POST, instance=manager)
        if form.is_valid():
            form.save()
            return redirect('/jantaadmin')

    context = {'form':form}
    return render(request, 'Janta/updatemanager.html', context)

@login_required(login_url='login')
def deletemanager(request, pk):
    manager = Manager.objects.get(id=pk)
    if request.method == 'POST':
        manager.delete()
        return redirect('/jantaadmin')

    context = {'manager':manager}
    return render(request, 'Janta/deletemanager.html', context)

@login_required(login_url='login')
def createwriter(request):
    form = AddWriterForm()
    if request.method == 'POST':
        form = AddWriterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/jantaadmin')

    context = {'form':form}
    return render(request, 'Janta/createwriter.html', context)

@login_required(login_url='login')
def updatewriter(request, pk):
    writer = Writer.objects.get(id=pk)
    form = AddWriterForm(instance=writer)
    if request.method == 'POST':
        form = AddWriterForm(request.POST, instance=writer)
        if form.is_valid():
            form.save()
            return redirect('/jantaadmin')

    context = {'form':form}
    return render(request, 'Janta/updatewriter.html', context)

@login_required(login_url='login')
def deletewriter(request, pk):
    writer = Writer.objects.get(id=pk)
    if request.method == 'POST':
        writer.delete()
        return redirect('/jantaadmin')

    context = {'writer':writer}
    return render(request, 'Janta/deletewriter.html', context)

@login_required(login_url='login')
def allorders(request):
    orders = Order.objects.all()
    myfilter = OrderFilter(request.GET, queryset=orders)
    orders = myfilter.qs

    context = {'orders':orders, 'myfilter':myfilter}
    return render(request, 'admin/orders.html', context)

@login_required(login_url='login')
def export_csv(request):
    current_date_time = datetime.now()
    orders = Order.objects.all()
    myfilter = OrderFilter(request.GET, queryset=orders)
    orders = myfilter.qs
    response = HttpResponse(
        content_type = 'text/csv',
        headers = {'Content-Disposition': f'attachment; filename="writer_orders {str(current_date_time)}.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow(['Order No.','Order Cpp','Pages','Email','Assignee'])

    for order in filter.values_list('Order No.','Order Cpp','Pages','Email','Assignee'):
        writer.writerow([order.order_id, order.cpp, order.pages, order.writer.Email, order.manager.Full_Names])

    return response 

def sendmail(request):
    MY_EMAIL = "vickmaish01@yahoo.com"
    MY_PASSWORD = "ythumelnjpiqasen"

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="victornjenga01@gmail.com ",
            msg=f"Subject:Order Report\n\n{MY_EMAIL}"
        )
    
    return response

def jantareports(request):

    context = {}
    return render(request, 'admin/reports.html', context)