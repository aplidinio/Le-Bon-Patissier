from django.db import models

# Create your models here.

from django import forms

# creating a form
class LoginForm(forms.Form):

	nombre = forms.CharField(max_length = 30)
	#last_name = forms.CharField(max_length = 30)
	#email = forms.EmailField(max_length = 50)	
	password = forms.CharField(widget = forms.PasswordInput())

