from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    subject = forms.CharField(min_length=5)
    message = forms.CharField(min_length=20, widget=forms.Textarea)
    class Meta:
        model = Contact
        exclude = ('user', 'answer')
