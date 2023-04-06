from django.db import models
from django.contrib.auth.models import User


# class State(models.Model):
#     state_id = models.IntegerField(primary_key=True)
#     state_name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.state_name
#
# class District(models.Model):
#     district_id = models.IntegerField(primary_key=True)
#     state_name = models.ForeignKey("State", on_delete=models.CASCADE)
#     district_name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.district_name
#
#
# class Taluka(models.Model):
#     taluka_id = models.IntegerField(primary_key=True)
#     state_name = models.ForeignKey("State", on_delete=models.CASCADE)
#     district_name = models.ForeignKey("District", on_delete=models.CASCADE)
#     taluka_name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.taluka_name


class Grampanchayat(models.Model):
    # state_name = models.ForeignKey("State", on_delete=models.CASCADE)
    # district_name = models.ForeignKey("District", on_delete=models.CASCADE)
    # taluka_name = models.ForeignKey("Taluka", on_delete=models.CASCADE)
    gramid = models.IntegerField(primary_key=True)
    gramname = models.CharField(max_length=50, unique=True)
    gramaddress = models.TextField(max_length=100)
    gramemail = models.EmailField()
    gramcontact = models.CharField(max_length=10)

    def __str__(self):
        return self.gramname

class Gramadmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grampanchayat = models.ForeignKey("Grampanchayat", on_delete=models.CASCADE)
    gramadminid = models.IntegerField(primary_key=True)
    gramadminmobno = models.CharField(max_length=10)
    gramadminphoto = models.FileField(upload_to='gramadmin/', null=True)

    def __str__(self):
        return self.user.username


class FamilyHead(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grampanchayat = models.ForeignKey("Grampanchayat", on_delete=models.CASCADE)
    familyheadid = models.IntegerField(primary_key=True)
    familyheadgender = models.CharField(max_length=6)
    birthdate = models.DateField()
    familyheadmobno = models.CharField(max_length=10)
    familyheadadharno = models.CharField(max_length=12)
    familyheadpanno = models.CharField(max_length=10)
    familyheadphoto = models.FileField(upload_to='family_head/', null=True)
    familyincome = models.CharField(max_length=15)
    rationcardtype = models.CharField(max_length=10)
    rationcardno = models.CharField(max_length=25)

    def __str__(self):
        return self.user.username


class Familymembers(models.Model):
    grampanchayat = models.ForeignKey("Grampanchayat", on_delete=models.CASCADE)
    family = models.ForeignKey("FamilyHead", on_delete=models.CASCADE)
    familymemberid = models.IntegerField()
    familymembername = models.CharField(max_length=40)
    relation = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    birthdate = models.DateField()
    aadharnop = models.CharField(max_length=12)
    familymemberphoto = models.FileField(upload_to='family_member/', null=True)

    def __str__(self):
        return self.familymembername


class Authority(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grampanchayat = models.ForeignKey("Grampanchayat", on_delete=models.CASCADE)
    authorityid = models.IntegerField(primary_key=True)
    authority = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    aadharnop = models.CharField(max_length=12)
    qualification = models.CharField(max_length=20)
    authoritynmobno = models.CharField(max_length=10)
    authorityphoto = models.FileField(upload_to='authority/', null=True)

    def __str__(self):
        return self.user.username


class BirthDetail(models.Model):
    childid = models.IntegerField(primary_key=True, serialize=False)
    childname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    birthdate = models.DateField()
    fathername = models.CharField(max_length=50)
    mothername = models.CharField(max_length=50)
    birthplace = models.CharField(max_length=30)
    registration_number = models.CharField(max_length=20)
    registration_date = models.DateField()

    def __str__(self):
        return self.childname


class WaterTax(models.Model):
    watertaxid = models.IntegerField(primary_key=True)
    waterconnectiontype = models.CharField(max_length=30, unique=True)
    watertaxrate = models.IntegerField()


class WaterConnection(models.Model):
    waterconnectionid = models.IntegerField(primary_key=True)
    waterconnectionno = models.IntegerField(unique=True)
    gram = models.ForeignKey("Grampanchayat", on_delete=models.CASCADE)
    region = models.CharField(max_length=20)
    subregion = models.CharField(max_length=20)
    waterconnectiontype = models.CharField(max_length=30)
    ownername = models.ForeignKey("FamilyHead", on_delete=models.CASCADE)

    def __str__(self):
        return self.ownername


class Houses(models.Model):
    houseid = models.IntegerField(primary_key=True)
    houseno = models.IntegerField(unique=True)
    gram = models.ForeignKey("Grampanchayat", on_delete=models.CASCADE)
    region = models.CharField(max_length=20)
    subregion = models.CharField(max_length=20)
    housetype = models.CharField(max_length=20)
    housearea = models.IntegerField()
    ownername = models.ForeignKey("FamilyHead", on_delete=models.CASCADE)


class Housetax(models.Model):
    housetypeid = models.IntegerField(primary_key=True)
    housetype = models.CharField(max_length=30, unique=True)
    hosetaxrate = models.IntegerField()
