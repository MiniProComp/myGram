from django.contrib import admin
from .models import Grampanchayat, Gramadmin, Child, FamilyHead,House

# Register your models here.
admin.site.register(Grampanchayat)
admin.site.register(Gramadmin)
admin.site.register(Child)
admin.site.register(FamilyHead)
admin.site.register(House)

