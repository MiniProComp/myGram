from django.contrib import admin
from .models import Grampanchayat, Gramadmin, Child, FamilyHead, State, District, Taluka

# Register your models here.
admin.site.register(State)
admin.site.register(District)
admin.site.register(Taluka)
admin.site.register(Grampanchayat)
admin.site.register(Gramadmin)
admin.site.register(Child)
admin.site.register(FamilyHead)

