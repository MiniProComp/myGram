import smtplib
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Grampanchayat, Gramadmin, Child, FamilyHead, Familymembers, House, Housetax, WaterTax
from django.db.models import Max
# from .forms import
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from email.message import EmailMessage
import pywhatkit


# Create your views here.
def home1(request):
    if request.method == "POST":
        receiver = request.POST["subscriber"]
        print(receiver)
        sender = "myGram"
        subject = "Subscribed to myGram"
        content = "Hello! You have successfully subscribed to myGram"
        sendmail(subject, sender, receiver, content)

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


def sendmail(subject, sender, receiver, content):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver
    msg.set_content(content)
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("miniprojectsecomp@gmail.com", "yptkvurskgdnrpiv")
    server.send_message(msg)
    server.quit()


def subscribe(request):
    receiver = request.POST["email"]
    print(receiver)
    # sender = "myGram"
    # subject = "Subscribed to myGram"
    # content = "Hello! You have successfully subscribed to myGram"
    # sendmail(subject, sender, receiver, content)
    return None

def addgram(request):
    current_user = request.user
    if current_user.is_superuser:
        gramid = 1001 if Grampanchayat.objects.count() == 0 else Grampanchayat.objects.aggregate(max=Max('gramid'))[
                                                                     "max"] + 1
        if request.method == "POST":
            gramname = request.POST['gramname']
            gramaddress = request.POST['gramaddress']
            gramemail = request.POST['gramemail']
            gramcontact = request.POST['gramcontact']

            ins = Grampanchayat.objects.create(gramid=gramid, gramname=gramname, gramaddress=gramaddress,
                                               gramemail=gramemail, gramcontact=gramcontact)
            ins.save()

            messages.success(request, '''Grampanchayat Successfully added...''')
            return redirect('home1')
        else:
            return render(request, 'gramapp/addGrampanchayat.html', locals())
    else:
        return render(request, 'gramapp/pageNotFound.html')


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
        eachGramAdmin = Gramadmin.objects.get(grampanchayat=gram)

        user = User.objects.all().filter(username=eachGramAdmin.user)
        eachGramAdmin.delete()
        user.delete()
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
        if gramadminpass == gramadmincnfmpass:
            myuser = User.objects.create_user(gramadminusername, gramadminemail, gramadminpass, is_staff=True)
            myuser.first_name = (gramadminfname)
            myuser.last_name = (gramadminlname)
            myuser.save()

            ins = Gramadmin.objects.create(user=myuser, grampanchayat=eachGram, gramadminid=gramadminid,
                                           gramadminmobno=gramadminmobno, gramadminphoto=gramadminphoto)
            ins.save()

            #Sending Email
            msg = EmailMessage()
            msg['Subject'] = 'Grampanchayat Admin username and password '
            msg['From'] = 'myGram'
            msg['To'] = gramadminemail
            msg.set_content(
                "Hello! \n" + gramadminfname + " " + gramadminlname + "\n This is an auto generated message from myGram \n "
                                                            "Don't share this with anyone \n"
                                                            "Your username is: " + gramadminusername +
                "\nPassword is:" + gramadminpass +
                " \nURL:")
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login("miniprojectsecomp@gmail.com", "yptkvurskgdnrpiv")
            server.send_message(msg)
            server.quit()
            content = "Hello! \n" + gramadminfname + " " + gramadminlname + "\n This is an auto generated message from myGram \n" \
                                                                        " ""Don't share this with anyone \n"\
                                                                        "Your username is: " + gramadminusername +\
                                                                        "\nPassword is:" + gramadminpass +" \nURL:"

            whatsappmessage(gramadminmobno, content)


            messages.success(request, '''Gramapanchayat dmin Successfully added...''')
            return redirect('home1')
        else:
            messages.error(request, '''Password does not match''')
            return redirect('addgramadmin')
    else:
        context = {'eachGram': eachGram}
        return render(request, 'gramapp/addgramadmin.html', context)


def whatsappmessage(mobno,message):
    mobno= mobno
    message= message
    pywhatkit.sendwhatmsg_instantly("+91" + mobno, message)



def viewGramAdmin(request, pk):
    eachGramAdmin = Gramadmin.objects.get(gramadminid=pk)
    eachUser = User.objects.get(username=eachGramAdmin.user)
    print(eachUser)
    context = {'eachGramAdmin': eachGramAdmin, 'eachUser': eachUser}
    return render(request, 'gramapp/viewGramAdmin.html', context)

def deletegramadmin(request, pk):
    eachGramAdmin = Gramadmin.objects.get(gramadminid=pk)
    user = User.objects.all().filter(username=eachGramAdmin.user)
    user.delete()
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


def addFamilyHead(request):
    familyheadid = 100001 if FamilyHead.objects.count() == 0 else FamilyHead.objects.aggregate(max=Max('familyheadid'))["max"] + 1
    grampanchayat = Grampanchayat.objects.all()
    if request.method == "POST" and request.FILES['familyheadphoto']:
        current_user = request.user
        if current_user.is_superuser:
            selectedgramid = request.POST['gram']
            gram = Grampanchayat.objects.get(gramid=selectedgramid)
        else:
            gramAdmin = Gramadmin.objects.get(user=current_user)
            adminGram = gramAdmin.grampanchayat
            gram = Grampanchayat.objects.get(gramname=adminGram)

        familyheadphoto = request.FILES['familyheadphoto']
        fss = FileSystemStorage('media/family_head/')
        familyheadfname = request.POST['familyheadfname']
        familyheadlname = request.POST['familyheadlname']
        familyheadgender = request.POST['familyheadgender']
        birthdate = request.POST['birthdate']
        familyheadmobno = request.POST['familyheadmobno']
        familyheademail = request.POST['familyheademail']
        familyheadadharno = request.POST['familyheadadharno']
        familyheadpanno = request.POST['familyheadpanno']
        familyincome = request.POST['familyincome']
        rationcardtype = request.POST['rationcardtype']
        rationcardno = request.POST['rationcardno']

        familyheadusername = request.POST['familyheadusername']
        familyheadpass = request.POST['familyheadpass']
        familyheadcnfmpass = request.POST['familyheadcnfmpass']

        myuser = User.objects.create_user(familyheadusername, familyheademail, familyheadpass)
        myuser.first_name = (familyheadfname)
        myuser.last_name = (familyheadlname)
        myuser.save()

        ins = FamilyHead.objects.create(user=myuser, grampanchayat=gram, familyheadid=familyheadid,
                                  familyheadgender=familyheadgender,birthdate=birthdate, familyheadmobno=familyheadmobno, familyheadadharno=familyheadadharno,
                                    familyheadpanno=familyheadpanno, familyheadphoto=familyheadphoto, familyincome=familyincome,
                                       rationcardtype=rationcardtype, rationcardno=rationcardno)
        ins.save()

        # Sending Email
        msg = EmailMessage()
        msg['Subject'] = 'Grampanchayat Family Head username and password '
        msg['From'] = 'myGram'
        msg['To'] = familyheademail
        msg.set_content(
            "Hello! \n" + familyheadfname + " " + familyheadlname + "\n This is an auto generated message from myGram \n "
                                                                  "Don't share this with anyone \n"
                                                                  "Your username is: " + familyheadusername +
                                                                    "\nPassword is:" + familyheadpass +
                                                                    " \nURL:")
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("miniprojectsecomp@gmail.com", "yptkvurskgdnrpiv")
        server.send_message(msg)
        server.quit()

        messages.success(request, '''Family Head Successfully added...''')
        return redirect('home1')
    else:
        context = {'grampanchayat': grampanchayat}
        return render(request, 'gramapp/addFamilyHead.html', context)


def addFamilymember(request):
    familymemberid = 100001 if Familymembers.objects.count() == 0 else Familymembers.objects.aggregate(max=Max('familymemberid'))["max"] + 1
    current_user = request.user

    if current_user.is_staff:
        if current_user.is_superuser:
            print("superuser")
        if not current_user.is_superuser:
            gramadmin = Gramadmin.objects.get(user=current_user)
            admingram = gramadmin.grampanchayat
            gram = Grampanchayat.objects.get(gramname=admingram)
            familyheads = FamilyHead.objects.all().filter(grampanchayat=gram)

            if request.method == "POST":
                familyheadid = request.POST['familyhead']
                family = FamilyHead.objects.get(familyheadid=familyheadid)
                familymemberfname = request.POST['familymemberfname']
                relation = request.POST['relation']
                familymembergender = request.POST['familymembergender']
                birthdate = request.POST['birthdate']
                familyheadadharno = request.POST['familyheadadharno']
                familymemberphoto = request.FILES['familymemberphoto']
                fss = FileSystemStorage('media/family_member/')

                ins = Familymembers.objects.create(grampanchayat=gram, family=family, familymemberid=familymemberid,
                                                familymembername=familymemberfname, relation=relation,
                                                gender=familymembergender, birthdate=birthdate,
                                                aadharnop=familyheadadharno, familymemberphoto=familymemberphoto,)
                ins.save()
                messages.success(request, '''Family Member Successfully added...''')
                return redirect('home1')
    else:
        print("no")

    context = {'familyheads': familyheads}
    return render(request, 'gramapp/addFamilymember.html', context)


def viewFamily(request):
    current_user = request.user
    gramadmin = Gramadmin.objects.get(user=current_user)
    admingram = gramadmin.grampanchayat
    gram = Grampanchayat.objects.get(gramname=admingram)
    familyheads = FamilyHead.objects.all().filter(grampanchayat=gram)
    context = {'familyheads': familyheads}
    return render(request, 'gramapp/viewFamily.html', context)


def viewFamilyDetails(request, pk):
    familyhead = FamilyHead.objects.get(familyheadid=pk)
    familymembers = Familymembers.objects.all().filter(family=familyhead)
    context = {'familyhead': familyhead, 'familymembers': familymembers}
    return render(request, 'gramapp/viewFamilyDetails.html', context)


def addScheme(request):
    return render(request, 'gramapp/addScheme.html')



def waterConnectioninfo(request):
    return render(request, 'gramapp/waterConnectioninfo.html')

def addWatertax(request):
    watertaxid = 301 if WaterTax.objects.count() == 0 else WaterTax.objects.aggregate(max=Max('watertaxid'))["max"] + 1
    if request.method == "POST":
        waterconnectiontype = request.POST['waterconnectiontype']
        watertaxrate = request.POST['watertaxrate']

        ins = Housetax.objects.create(watertaxid=watertaxid, waterconnectiontype=waterconnectiontype, watertaxrate=watertaxrate)
        ins.save()
        messages.success(request, '''Water Tax Details Successfully added...''')
        return redirect('home1')
    else:
        print("no")
    return render(request, 'gramapp/addWatertax.html')

def addHouse(request):
    houseid = 200001 if House.objects.count() == 0 else House.objects.aggregate(max=Max('houseid'))["max"] + 1
    current_user = request.user
    gramadmin = Gramadmin.objects.get(user=current_user)
    admingram = gramadmin.grampanchayat
    gram = Grampanchayat.objects.get(gramname=admingram)
    familyheads = FamilyHead.objects.all().filter(grampanchayat=gram)

    if request.method == "POST":
        houseno = request.POST['houseno']
        region = request.POST['region']
        subregion = request.POST['subregion']
        housetype = request.POST['housetype']
        housearea = request.POST['housearea']
        familyheadid = request.POST['ownername']
        ownername = FamilyHead.objects.get(familyheadid=familyheadid)
        ins = House.objects.create(houseno=houseno, gram=gram, houseid=houseid, region=region, subregion=subregion,
                                           housetype=housetype, housearea=housearea,
                                           ownername=ownername)
        ins.save()
        messages.success(request, '''House Successfully added...''')
        return redirect('home1')
    else:
        context = {'familyheads': familyheads}
    return render(request, 'gramapp/addHouse.html', context)


def addHousetax(request):
    housetypeid = 201 if Housetax.objects.count() == 0 else Housetax.objects.aggregate(max=Max('housetypeid'))["max"] + 1
    if request.method == "POST":
        housetype = request.POST['housetype']
        hosetaxrate = request.POST['hosetaxrate']

        ins = Housetax.objects.create(housetypeid=housetypeid, housetype=housetype, hosetaxrate=hosetaxrate)
        ins.save()
        messages.success(request, '''House Tax Details Successfully added...''')
        return redirect('home1')
    else:
        print("no")
    return render(request, 'gramapp/addHousetax.html')

def houseDetails(request):
    current_user = request.user
    familyhead = FamilyHead.objects.get(user=current_user)
    houses = House.objects.all().filter(ownername=familyhead)
    context = {'houses': houses}

    return render(request, 'gramapp/houseDetails.html',context)






