from django.forms import DateInput, ModelForm
from . models import Contact
from django import forms

# my forms will go here

class ContactForm(ModelForm):
    
    class Meta :
        model = Contact
        fields = "__all__"