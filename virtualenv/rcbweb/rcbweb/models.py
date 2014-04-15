from django.db import models
from django.forms import ModelForm

# Create your models here.
class RCBUser(models.Model):
    username = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=128)
    cookiekey = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    isactive = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username

class RegistrationForm(ModelForm):
    class Meta:
        model = RCBUser
        fields = ['username', 'password', 'email']

class LoginForm(ModelForm):
    class Meta:
        model = RCBUser
        fields = ['username', 'password']