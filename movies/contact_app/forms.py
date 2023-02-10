from django import forms
from .models import Contact
from captcha.fields import CaptchaField

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    
    class Meta:
        model = Contact
        fields= ['email']
        widgets = {
            'email':forms.EmailInput(attrs={'id':'form5Example21', 'class':'form-control'}),'captcha':forms.TextInput(attrs={'class':'form-control'})
        }