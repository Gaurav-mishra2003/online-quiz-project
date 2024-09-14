from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


class quiz_form(forms.Form):
    question=forms.CharField(max_length=200)
    opption1=forms.CharField(max_length=100)
    opption2=forms.CharField(max_length=100)
    opption3=forms.CharField(max_length=100)
    opption4=forms.CharField(max_length=100)
    answer=forms.CharField(max_length=100)

class answer_form(forms.Form):
    Answer=forms.CharField(max_length=80)
    

class signupform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name'] 
    
       
 
    
