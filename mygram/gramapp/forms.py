from django import forms
from .models import Grampanchayat


class companyforms(forms.ModelForm):
    class Meta:
        model = Grampanchayat
        fields = "__all__"
