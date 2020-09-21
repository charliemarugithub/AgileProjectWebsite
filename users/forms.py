import datetime

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Subscription


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class SubscriptionForm(forms.ModelForm):
    firstName = forms.CharField(
        required=True,
        label="First Name",
        widget=forms.TextInput(attrs={
                'type':"text",
                'placeholder':"First name",
                'class':'form-control', # html input class
        })
    )

    lastName = forms.CharField(
        required=True,
        label="Last Name",
        widget=forms.TextInput(attrs={
                'type':"text",
                'placeholder':"Last name",
                'class':'form-control', # html input class
        })
    )

    username = forms.CharField(
        required=True,
        label="Username",
        widget=forms.TextInput(attrs={
                'type':"text",
                'placeholder':"Username",
                'class':'form-control', # html input class
        })
    )

    sub_type = forms.ChoiceField(
        required=True,
        label="Subscription Type",
        choices=(
            ('Option 1', 'Choose...'),
            ('Weekly $ Free', 'Weekly $ Free'),
            ('Monthly $10', 'Monthly $10'),
            ('Annual $100', 'Annual $100'),
        ),
        widget=forms.Select(attrs={
                'type':"text",
                'placeholder':"Subscription Type",
                'class':'custom-select d-block w-100', # html input class
        })
    )

    email = forms.CharField(
        required=True,
        label="Email",
        widget=forms.TextInput(attrs={
                'type':"text",
                'placeholder':"Email",
                'class':'form-control', # html input class
        })
    )

    address = forms.CharField(
        required=True,
        label="Address",
        widget=forms.TextInput(attrs={
                'type':"text",
                'placeholder':"Address",
                'class':'form-control', # html input class
        })
    )

    address2 = forms.CharField(
        required=True,
        label="Address2",
        widget=forms.TextInput(attrs={
                'type':"text",
                'placeholder':"Address",
                'class':'form-control', # html input class
        })
    )

    state = forms.ChoiceField(
        required=True,
        label="City",
        choices=(
            ('Choose', 'Choose'),
            ('Auckland', 'Auckland'),
            ('Christchurch', 'Christchurch'),
            ('Wellington', 'Wellington'),
        ),
        widget=forms.Select(attrs={
                'type':"text",
                'placeholder':"State",
                'class':'custom-select d-block w-100', # html input class
        })
    )

    country = forms.ChoiceField(
        required=True,
        label="Country",
        choices=(
            ('Option 1', 'Choose'),
            ('Option 2', 'New Zealand'),
            ('Option 3', 'Australia'),
            ('Option 2', 'Amsterdam'),
        ),
        widget=forms.Select(attrs={
            'type': "text",
            'placeholder': "Country",
            'class': 'custom-select d-block w-100',  # html input class
        })
    )

    postcode = forms.CharField(
        required=True,
        label="Postcode",
        widget=forms.TextInput(attrs={
                'type':"text",
                'placeholder':"Postcode",
                'class':'form-control', # html input class
        })
    )

    same_address = forms.BooleanField(
        required=False,
        label="Shipping address is the same as my billing address",
        widget=forms.CheckboxInput(attrs={
                'type':"checkbox",
                'class':'CheckboxInput', # html input class
        })
    )

    save_info = forms.BooleanField(
        required=False,
        label="Save this information for next time",
        widget=forms.CheckboxInput(attrs={
                'type':"checkbox",
                'class':'CheckboxInput', # html input class
        })
    )

    date_of_signup = forms.DateField(
        required=True,
        label="Date of Sign Up",
        initial=datetime.datetime.now(),
        widget=forms.SelectDateWidget(attrs={
            'disabled': False,
            'readonly': True,

        })

    )

    class Meta:
        model = Subscription
        fields = [
            'firstName',
            'lastName',
            'username',
            'sub_type',
            'email',
            'address',
            'address2',
            'state',
            'country',
            'postcode',
            'same_address',
            'save_info',
            'date_of_signup',
        ]
