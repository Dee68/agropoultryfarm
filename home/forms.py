from django import forms
from django.db.models import fields
from .models import ContactMessage, SubscribedUser

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email','subject','message']
        labels = {
            'name':'',
            'email':'',
            'subject':'',
            'message':''
        }
        forms.widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','id':'fname','placeholder':'Your fullname'}),
        'email':forms.TextInput(attrs={'class':'form-control','id':'email','placeholder':'Your email address'}),
        'subject':forms.TextInput(attrs={'class':'form-control','id':'subject','placeholder':'Your subject of this message'}),
        'message':forms.Textarea(attrs={'class':'form-control','id':'message','placeholder':'Your message','rows':8})
        }

class SubscribersForm(forms.ModelForm):
    class Meta:
        model = SubscribedUser
        fields = ['email']
        labels ={
            'email':''
        }
        forms.widgets = {
            'email':forms.EmailInput(attrs={'class':'form-control','id':'email','placeholder':'Email','required':'required'})
        }