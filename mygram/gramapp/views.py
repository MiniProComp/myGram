from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Grampanchayat, Gramadmin, Child,Spot,Housetaxinfo,House
from django.db.models import Max
# from .forms import
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home1(request):
    return render(request, 'gramapp/home1.html')


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


def addgram(request):
    gramid = 1001 if Grampanchayat.objects.count() == 0 else Grampanchayat.objects.aggregate(max=Max('gramid'))["max"] + 1
    if request.method == "POST":
        gramname = request.POST['gramname']
        gramaddress = request.POST['gramaddress']
        gramemail = request.POST['gramemail']
        gramcontact = request.POST['gramcontact']

        ins = Grampanchayat.objects.create(gramid=gramid, gramname=gramname, gramaddress=gramaddress, gramemail=gramemail, gramcontact=gramcontact)
        ins.save()

        messages.success(request, '''Grampanchayat Successfully added...''')
        return render(request, 'gramapp/home1.html')
    else:
        return render(request, 'gramapp/addGrampanchayat.html', locals())



def viewgram(request):
    grampanchayat = Grampanchayat.objects.all()
    context = {'grampanchayat': grampanchayat}
    return render(request, 'gramapp/viewGrampanchayat.html', context)


def gramdetail(request, pk):
    eachGram = Grampanchayat.objects.get(gramid=pk)
    gramAdmin = Gramadmin.objects.all().filter(grampanchayat=eachGram)
    context = {'eachGram': eachGram, 'gramAdmin': gramAdmin}
    return render(request, 'gramapp/viewGramDetails.html', context)

def deletegram(request, pk):
    gram = Grampanchayat.objects.get(gramid=pk)

    try:
        eachGramAdmin = Gramadmin.objects.all().filter(grampanchayat=gram)
        eachGramAdmin.delete()
        gram.delete()
    except:
        gram.delete()
    messages.success(request, '''Grampanchayat Successfully deleted...''')
    return redirect('home1')


def addgramadmin(request, pk):
    gramadminid = 5001 if Gramadmin.objects.count() == 0 else Gramadmin.objects.aggregate(max=Max('gramadminid'))["max"] + 1
    eachGram = Grampanchayat.objects.get(gramid=pk)
    if request.method == "POST" and request.FILES['gramadminphoto']:
        gramadminphoto = request.FILES['gramadminphoto']
        fss = FileSystemStorage('media/gramadmin/')
        gramadminfname = request.POST['gramadminfname']
        gramadminlname = request.POST['gramadminlname']
        gramadminmobno = request.POST['gramadminmobno']
        gramadminemail = request.POST['gramadminemail']
        gramadminusername = request.POST['gramadminusername']
        gramadminpass = request.POST['gramadminpass']
        gramadmincnfmpass = request.POST['gramadmincnfmpass']

        myuser = User.objects.create_user(gramadminusername, gramadminemail, gramadminpass)
        myuser.first_name = (gramadminfname)
        myuser.last_name = (gramadminlname)
        myuser.save()

        ins = Gramadmin.objects.create(user=myuser, grampanchayat=eachGram, gramadminid=gramadminid,
                                  gramadminmobno=gramadminmobno, gramadminphoto=gramadminphoto)
        ins.save()

        # msg = EmailMessage()
        # msg['Subject'] = 'spoc username and password '
        # msg['From'] = 'compliPro'
        # msg['To'] = spocemail
        # msg.set_content(
        #     "Hello! \n" + spocfname + " " + spoclname + "\n This is an auto generated message from compliPro \n "
        #                                                 "Don't share this with anyone \n"
        #                                                 "Your username is: " + spocusername +
        #     "\nPassword is:" + spocpass +
        #     " \nURL:")
        # server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        # server.login("miniprojectsecomp@gmail.com", "btkfbakhglqhasoo")
        # server.send_message(msg)
        # server.quit()
        messages.success(request, '''SPOC Successfully added...''')
        return render(request, 'gramapp/home1.html')
    else:
        context = {'eachGram': eachGram}
        return render(request, 'gramapp/addgramadmin.html', context)


def viewGramAdmin(request, pk):
    eachGramAdmin = Gramadmin.objects.get(gramadminid=pk)
    eachUser = User.objects.get(username=eachGramAdmin.user)
    print(eachUser)
    context = {'eachGramAdmin': eachGramAdmin, 'eachUser': eachUser}
    return render(request, 'gramapp/viewGramAdmin.html', context)

def deletegramadmin(request, pk):
    eachGramAdmin = Gramadmin.objects.get(gramadminid=pk)
    eachGramAdmin.delete()
    messages.success(request, '''Grampanchayat Admin Successfully deleted...''')
    return redirect('home1')


def addBirthDetails(request):
    childid = 1001 if Child.objects.count() == 0 else Child.objects.aggregate(max=Max('childid'))["max"] + 1
    if request.method == "POST" and request.FILES['birthproof']:
        childname = request.POST['childname']
        gender = request.POST['gender']
        birthdate = request.POST['birthdate']
        fathername = request.POST['fathername']
        mothername = request.POST['mothername']
        birthplace = request.POST['birthplace']
        registeredon = request.POST['registeredon']
        birthproof = request.FILES['birthproof']
        fss = FileSystemStorage('media/birthproof/')


        ins = Child.objects.create(childid=childid, childname=childname, gender=gender, birthdate=birthdate,
                                   fathername=fathername, mothername=mothername, birthplace=birthplace, registeredon=registeredon,
                                   birthproof=birthproof)
        ins.save()

        messages.success(request, '''New Child Registration Successfully added...''')
        return render(request, 'gramapp/home1.html')
    else:
        return render(request, 'gramapp/addBirthDetails.html', locals())


def addAuthority(request):
    return render(request, 'gramapp/addAuthority.html')

def addComplaint(request):
    return render(request, 'gramapp/addComplaint.html')

def addFamily(request):
    return render(request, 'gramapp/addFamily.html')

def addFamilymember(request):
    return render(request, 'gramapp/addFamilymember.html')

def addHouse(request):
    houseid = 1001 if House.objects.count() == 0 else House.objects.aggregate(max=Max('houseid'))[
                                                                     "max"] + 1
    if request.method == "POST":
        vibhag = request.POST['vibhag']
        vadi = request.POST['vadi']
        housetype = request.POST['housetype']
        housedimension = request.POST['housedimension']
        ownername = request.POST['ownername']

        ins = House.objects.create(houseid=houseid, vibhag=vibhag, vadi=vadi, housetype=housetype,
                                   housedimension=housedimension, ownername=ownername,)
        ins.save()

        messages.success(request, '''New House Is Successfully added...''')
        return render(request, 'gramapp/home1.html')
    else:
        return render(request, 'gramapp/addHouse.html', locals())



def addHousetax(request):
    housetypeid = 1001 if Housetaxinfo.objects.count() == 0 else Housetaxinfo.objects.aggregate(max=Max('housetypeid'))["max"] + 1
    if request.method == "POST":
        housetype = request.POST['housetype']
        hosetaxrate = request.POST['hosetaxrate']

        ins = Housetaxinfo.objects.create(housetypeid=housetypeid, housetype=housetype, hosetaxrate=hosetaxrate)
        ins.save()

        messages.success(request, '''Tax Related Inforation Is Successfully added...''')
        return render(request, 'gramapp/home1.html')
    else:
        return render(request, 'gramapp/addHousetax.html', locals())


def addMarriageinfo(request):
    return render(request, 'gramapp/addMarriageinfo.html')

def addScheme(request):
    return render(request, 'gramapp/addScheme.html')

def addSpot(request):
    spotid = 11001 if Spot.objects.count() == 0 else Spot.objects.aggregate(max=Max('spotid'))["max"] + 1
    if request.method == "POST":
        spottype = request.POST['spottype']
        spotname = request.POST['spotname']
        spotlocation = request.POST['spotlocation']
        spotimage = request.POST['spotimage']
        spotdescription = request.POST['spotdescription']

        ins = Spot.objects.create(spotid=spotid, spottype=spottype, spotname=spotname,
                                  spotlocation=spotlocation,
                                  spotimage=spotimage, spotdescription=spotdescription)
        ins.save()

        messages.success(request, '''Spot Successfully added...''')
        return render(request, 'gramapp/home1.html')
    else:
        return render(request, 'gramapp/addSpot.html', locals())


def waterConnectioninfo(request):
    return render(request, 'gramapp/waterConnectioninfo.html')

def addWatertax(request):
    return render(request, 'gramapp/addWatertax.html')

