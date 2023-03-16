from django.db import models
from django.contrib.auth.models import User


class State(models.Model):
    state_id = models.IntegerField(primary_key=True)
    state_name = models.CharField(max_length=50)

    def __str__(self):
        return self.state_name

class District(models.Model):
    district_id = models.IntegerField(primary_key=True)
    state_name = models.ForeignKey("State", on_delete=models.CASCADE)
    district_name = models.CharField(max_length=50)

    def __str__(self):
        return self.district_name


class Taluka(models.Model):
    taluka_id = models.IntegerField(primary_key=True)
    state_name = models.ForeignKey("State", on_delete=models.CASCADE)
    district_name = models.ForeignKey("District", on_delete=models.CASCADE)
    taluka_name = models.CharField(max_length=50)

    def __str__(self):
        return self.taluka_name


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
    familymemberphoto = models.FileField(upload_to='familyhead/', null=True)

    def __str__(self):
        return self.familyyheadname


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


class Child(models.Model):
    childid = models.IntegerField(primary_key=True)
    childname = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    birthdate = models.DateField(max_length=10)
    fathername = models.CharField(max_length=10)
    mothername = models.CharField(max_length=10)
    birthplace = models.CharField(max_length=10)
    registeredon = models.CharField(max_length=10)
    birthproof = models.FileField(upload_to='birthproof/', null=True)

    def __str__(self):
        return self.user.childname


class WaterTax(models.Model):
    watertaxid = models.IntegerField(primary_key=True)
    waterconnectiontype = models.CharField(max_length=10)
    watertaxrate = models.CharField(max_length=20)


class WaterConnection(models.Model):
    waterconnectionid = models.IntegerField(primary_key=True)
    ownername = models.ForeignKey("FamilyHead", on_delete=models.CASCADE)
    waterconnectiontype = models.CharField(max_length=10)

    def __str__(self):
        return self.user.ownername


