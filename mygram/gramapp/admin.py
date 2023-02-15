from django.contrib import admin
from .models import Grampanchayat, Gramadmin, Child

# Register your models here.
admin.site.register(Grampanchayat)
admin.site.register(Gramadmin)
admin.site.register(Child)

