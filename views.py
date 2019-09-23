from django.shortcuts import render,redirect
import sqlite3
from django.contrib.auth.models import User, auth
from .models import FlightDetails
# Create your views here.

def admin(request):
    print("----- In admin.admin ------")
    
    if request.method=='POST':
        data=request.POST
        username=data['username']
        password=data['password']
        u = next((u for u in UserDetails.objects.filter(uname=username)),None)
        print(u)
        print ("-------- ")
        
        #        return render(request, "wrongpassword.html")
        
        if u.uname!= 'admin':
            print("No such user")
            return render(request, "NoAccessPage.html")
        elif u.pswd != password:
            return render(request, "wrongpassword.html")
        
        return render(request, "adminpage.html")
    
    else:
        return render(request,"mainlogin.html")

def main(request):
    return render(request,'mainlogin.html')

#def adminPage(request):
    #return render(request,'adminpage.html')


# Create your views here.

#storing the flight data
def addflight(request):
    if request.method=='POST':
        data=request.POST
        From=data['from']
        to=data['to']
        flight_no=data['flight_no']
        flight_name=data['flight_name']
        no_of_seats=data['no_of_seats']
        Class=data['class']
        time=data['time']
        print("---- About to insert data ------")
        flight = FlightDetails(From=From, To=to, FlightNo=flight_no, FlightName=flight_name, NoOfSeats=no_of_seats, Class=Class, Time=time)
        flight.save()


    return redirect('adminpage.html')
  

def admin(request):
    return render(request,'adminpage.html')

