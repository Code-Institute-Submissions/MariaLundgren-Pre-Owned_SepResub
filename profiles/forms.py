from django import forms
from .models import UserProfile
from django.core.validators import RegexValidator


class UserProfileForm(forms.ModelForm):

    phone_regex = RegexValidator(regex=r'[0-9+]$', message=("You can only \
                                 enter numbers and + in this field."))
    postcode_regex = RegexValidator(regex=r'[0-9]$', message=("You can only \
                                    enter numbers in this field."))
    num_let_regex = RegexValidator(regex=r'[A-Za-z0-9]$', message=("You can \
                                   only enter letters and numbers in \
                                   this field."))

    default_name = forms.CharField(validators=[num_let_regex],
                                   required=True, min_length=5)
    default_phone_number = forms.CharField(validators=[phone_regex],
                                           required=True, min_length=5)
    default_street_address = forms.CharField(validators=[num_let_regex],
                                             required=True, min_length=5)
    default_postcode = forms.CharField(validators=[postcode_regex],
                                       required=True, min_length=4)
    default_town_or_city = forms.CharField(validators=[num_let_regex],
                                           required=True, min_length=4)

    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'default_name': 'Name',
            'default_phone_number': 'Phone Number',
            'default_street_address': 'Street Address',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_country': 'Country',
        }

        for field in self.fields:
            placeholder = f'{placeholders[field]} *'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
