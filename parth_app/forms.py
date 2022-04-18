
from re import S
from django import forms
class formupload(forms.Form):
    firstname=forms.CharField(label="Enter First Name",max_length=50)
    lastname=forms.CharField(label="Enter Last Name",max_length=50)
    email=forms.EmailField(label="Enter Your Email")
    file=forms.FileField()
from .models import contactform1

class formcontactform(forms.ModelForm):
    class Meta:
        model=contactform1
        fields=["fullname","email","contact","message" ]    
