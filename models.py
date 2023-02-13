from django.db import models
from django.contrib.auth.models import User

class Grampanchayat(models.Model):
    gramid = models.IntegerField(primary_key=True)
    gramname = models.CharField(max_length=50)
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


class Family(models.Model):
    grampanchayat = models.ForeignKey("Grampanchayat", on_delete=models.CASCADE)
    familyid = models.IntegerField(primary_key=True)
    familyheadid = models.IntegerField()
    familyheadname = models.CharField(max_length=40)
    gender = models.CharField(max_length=10)
    birthdate = models.DateField()
    aadharnop = models.CharField(max_length=12)
    familyheadphoto = models.FileField(upload_to='familyhead/', null=True)

    def __str__(self):
        return self.familyyheadname


class Familymembers(models.Model):
    grampanchayat = models.ForeignKey("Grampanchayat", on_delete=models.CASCADE)
    family = models.ForeignKey("Family", on_delete=models.CASCADE)
    familymemberid = models.IntegerField()
    familymembername = models.CharField(max_length=40)
    relation = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    birthdate = models.DateField()
    aadharnop = models.CharField(max_length=12)
    familymemberphoto = models.FileField(upload_to='familyhead/', null=True)

    def __str__(self):
        return self.familyyheadname
