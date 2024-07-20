from django import forms

from .models import Category, add_vehicle
from django.contrib.auth.forms import PasswordChangeForm

class categoryform(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['parking_area_no', 'vehicle_type', 'vehicle_limit', 'parking_charge']

        widgets = {
            'parking_area_no' : forms.TextInput(attrs={'class':'form-control'}),
            'vehicle_type': forms.TextInput(attrs={'class': 'form-control'}),
            'vehicle_limit': forms.TextInput(attrs={'class': 'form-control'}),
            'parking_charge': forms.TextInput(attrs={'class': 'form-control'}),

        }

class add_vehicleform(forms.ModelForm):
    class Meta:
        model = add_vehicle
        fields = ['vehicle_no','parking_area_no', 'vehicle_type', 'parking_charge']

        widgets = {
            'vehicle_no' : forms.TextInput(attrs={'class':'form-control'}),
            'parking_area_no' : forms.TextInput(attrs={'class':'form-control'}),
            'vehicle_type': forms.TextInput(attrs={'class': 'form-control'}),
            'parking_charge': forms.TextInput(attrs={'class': 'form-control'}),
        }


from django.contrib.auth.forms import PasswordChangeForm
from django import forms

class CustomPasswordChangeForm(PasswordChangeForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="New Password",
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm New Password",
    )
