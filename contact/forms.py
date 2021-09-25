from django import forms
from .models import Contact
from django.db.models.fields import BLANK_CHOICE_DASH

SUBJECT_CHOICES = [
    ('returns', 'Returns'),
    ('shipping', 'Shipping'),
    ('product_question', 'Product question'),
    ('other', 'Other')
]


class ContactForm(forms.ModelForm):
    subject = forms.CharField(widget=forms.Select(choices=BLANK_CHOICE_DASH + list(SUBJECT_CHOICES)))
    message = forms.CharField(min_length=20, widget=forms.Textarea)
    class Meta:
        model = Contact
        exclude = ('user', 'answer')
