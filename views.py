from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Max

# Create your views here.
def home1(request):
    return render(request,'home1.html')

def addGram(request):
    return render(request,'addGram.html')
def addAdmin(request):
    return render(request,'addAdmin.html')
def addFamily(request):
    return render(request,'addFamily.html')
def addFamilymember(request):
    return render(request,'addFamilymember.html')
def addHouse(request):
    return render(request,'addHouse.html')
def addAuthority(request):
    return render(request,'addAuthority.html')
def addSpot(request):
    return render(request,'addSpot.html')
def addHousetax(request):
    return render(request,'addHousetax.html')
def addWatertax(request):
    return render(request,'addWatertax.html')
def Waterconnectioninfo(request):
    return render(request,'Waterconnectioninfo.html')
def addRoad(request):
    return render(request,'addRoad.html')
def addScheme(request):
    return render(request,'addScheme.html')
def addBirthinfo(request):
    return render(request,'addBirthinfo.html')
def addMarriageinfo(request):
    return render(request,'addMarriageinfo.html')
def addComplaint(request):
    return render(request,'addComplaint.html')








def handlelogin(request):
    if request.method == "POST":
        loginemail = request.POST['loginemail']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginemail, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, '''You Have Successfully Logged In..''')
            return redirect('home1')
        else:
            messages.error(request, '''Incorrect Email or Password..''')
            return redirect('home1')
    return HttpResponse('404')


def handlelogout(request):
    logout(request)
    messages.success(request, '''You Have Successfully Logged Out..''')
    return redirect('home1')
