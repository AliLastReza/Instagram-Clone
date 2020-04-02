from django import forms
from django.contrib.auth import get_user_model
from django.forms import TextInput
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth import authenticate

from user.tasks import send_sms_api_kavenegar

User = get_user_model()


class RegistrationForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField(max_length=250)
    password = forms.CharField(widget=forms.PasswordInput)
    phone_number = forms.CharField()

    def clean(self):
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError(_("user Already Exists"))

        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(_("email Already Exists"))

        if User.objects.filter(phone_number=self.cleaned_data['phone_number']).exists():
            raise forms.ValidationError(_("Phone Number Is Registered"))
        return self.cleaned_data

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        send_sms_api_kavenegar.delay(user.username)
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        user = User.objects.filter(username=self.cleaned_data['username']).first()
        if user is None:
            raise forms.ValidationError("User Is Wrong")
        user = authenticate(**self.cleaned_data)
        if user is None:
            raise forms.ValidationError("Some THing Is Wrong")
        self.cleaned_data['user'] = user
        return self.cleaned_data
