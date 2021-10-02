from django import forms
from .models import Contact
from django.db.models.fields import BLANK_CHOICE_DASH
from django.utils.translation import ugettext_lazy as _

SUBJECT_CHOICES = [
    ('returns', 'Returns'),
    ('shipping', 'Shipping'),
    ('product_question', 'Product question'),
    ('other', 'Other')
]


class ContactForm(forms.ModelForm):
    subject = forms.CharField(widget=forms.Select(choices=BLANK_CHOICE_DASH +
                              list(SUBJECT_CHOICES)))
    message = forms.CharField(min_length=20, widget=forms.Textarea)

    class Meta:
        model = Contact
        exclude = ('user', 'answer')

        help_texts = {
            'order': _('If your message is concerning a specific order,\
                please choose the order number to make it easier and\
                faster for us to awnser you.'),
        }
