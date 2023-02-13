from django.contrib import admin
from .models import Grampanchayat, Gramadmin, Child, Spot, Housetaxinfo, House

# Register your models here.
admin.site.register(Grampanchayat)
admin.site.register(Gramadmin)
admin.site.register(Child)
admin.site.register(Spot)
admin.site.register(Housetaxinfo)
admin.site.register(House)
