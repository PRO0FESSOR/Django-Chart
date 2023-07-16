from django import forms 
from django.contrib.auth.forms import AuthenticationForm , UsernameField
from django.utils.translation import gettext , gettext_lazy as _
from .models import Profile


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control','autofocus': True}))
    password = forms.CharField(label=_("password"), strip = False ,widget=forms.PasswordInput(attrs={'autocomplete' : 'current-password','class':'form-control'}))

class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ('name','email','bio','age')
        widgets = {
            'name': forms.TextInput(attrs={'class' : 'form-control'}),
            'email': forms.EmailInput(attrs={'class' : 'form-control'}),
            'bio': forms.TextInput(attrs={'class' : 'form-control'}),
            'age': forms.TextInput(attrs={'class' : 'form-control'}),            
        }
