from django.contrib import admin
from .models import Grampanchayat, Gramadmin, Child, FamilyHead,Familymembers, Authority, WaterTax, WaterConnection
# Register your models here.
admin.site.register(Grampanchayat)
admin.site.register(Gramadmin)
admin.site.register(Child)
admin.site.register(FamilyHead)
admin.site.register(Familymembers)
admin.site.register(Authority)
admin.site.register(WaterTax)
admin.site.register(WaterConnection)



