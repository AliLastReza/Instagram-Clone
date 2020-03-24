from django import forms
from django.contrib.auth import get_user_model, authenticate, login
from django.utils.translation import ugettext_lazy as _

from user.utils import send_confirm_email, send_confirm_code

User = get_user_model()


class RegistrationForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError(_("username already exists"))

        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(_("email already exists"))
        return self.cleaned_data

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        send_confirm_email(user)
        send_confirm_code(user)
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        user = User.objects.filter(username=self.cleaned_data['username']).first()
        if user is None:
            raise forms.ValidationError(_("User with provided username does not exists"))

        # if not user.check_password(self.cleaned_data['password']):
        #     raise forms.ValidationError(_("Wrong password"))

        user = authenticate(**self.cleaned_data)
        if user is None:
            raise forms.ValidationError(_("Unable login with provided credentials"))
        self.cleaned_data['user'] = user
        return self.cleaned_data
