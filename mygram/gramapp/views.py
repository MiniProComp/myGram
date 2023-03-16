from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Grampanchayat, Gramadmin, Child, FamilyHead, Familymembers
from django.db.models import Max
# from .forms import
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from email.message import EmailMessage
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
        return redirect('home1')
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
            myuser = User.objects.create_user(gramadminusername, gramadminemail, gramadminpass)
            myuser.first_name = (gramadminfname)
            myuser.last_name = (gramadminlname)
            myuser.save()

            ins = Gramadmin.objects.create(user=myuser, grampanchayat=eachGram, gramadminid=gramadminid,
                                           gramadminmobno=gramadminmobno, gramadminphoto=gramadminphoto)
            ins.save()

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
            server.login("miniprojectsecomp@gmail.com", "btkfbakhglqhasoo")
            server.send_message(msg)
            server.quit()
            messages.success(request, '''Family Head Successfully added...''')
            return redirect('home1')
        else:
            messages.error(request, '''Password does not match''')
            return redirect('addgramadmin')
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
    return render(request, 'gramapp/addWatertax.html')

def addHousetax(request):
    return render(request, 'gramapp/addHousetax.html')

def addHouse(request):
    return render(request, 'gramapp/addHouse.html')




def addHouse(request):
    return render(request, 'gramapp/addHouse.html')


def addHousetax(request):
    return render(request, 'gramapp/addHousetax.html')