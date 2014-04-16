from django.db import models
from django import forms
from django.forms import ModelForm

# Create your models here.
class RCBUser(models.Model):
    username = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=128)
    osuser = models.CharField(max_length=128)
    ospassword = models.CharField(max_length=128)
    ostenantname = models.CharField(max_length=128)
    cookiekey = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    isadmin = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username

class RegistrationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    ospassword = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = RCBUser
        fields = ['username', 'password', 'email', 'osuser', 'ospassword', 'ostenantname']

class LoginForm(ModelForm):
    class Meta:
        model = RCBUser
        fields = ['username', 'password']