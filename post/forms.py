
from django import forms
from django_countries.fields import CountryField

PAYMENT_CHOICES = (
    ("S", 'Stripe'),
    ('P', 'PayPal')
)


class CheckoutForm(forms.Form):
    address =forms.CharField(required=False)
    address2 = forms.CharField(required=False)
    country = CountryField(blank_label = 'select country').formfield(required=False, attrs={
        
        'class': 'custom-select d-block w-100',
        
    })
    zip = forms.CharField(required=False)
    same_shipping_address =forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)    
    payment_option = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_CHOICES)

