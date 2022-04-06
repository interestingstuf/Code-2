import email
from django import forms
class formupload(forms.Form):
    firstname=forms.CharField(label="Enter First Name",max_length=50)
    lastname=forms.CharField(label="Enter Last Name",max_length=50)
    email=forms.EmailField(label="Enter Your Email", max_length=75)
    file=forms.FileField()