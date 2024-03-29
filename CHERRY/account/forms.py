from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from phonenumber_field.formfields import PhoneNumberField


class UserRegistrationForm(forms.Form):
    username = PhoneNumberField(label='شماره‌موبایل',  widget=forms.TextInput(
        attrs={'class': 'form-control eng'}), error_messages={
        'invalid': 'فرمت شماره‌موبایل نادرست است. فرمت درست: +989123456789 یا 09123456789'
    })
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput(
        attrs={'class': 'form-control eng'}), error_messages={
            'invalid': 'ساختار ایمیل نادرست است.'
    })
    password = forms.CharField(label='کلمه عبور', widget=forms.PasswordInput(
        attrs={'class': 'form-control eng'}))
    confirm_password = forms.CharField(label='تکرار کلمه عبور', widget=forms.PasswordInput(
        attrs={'class': 'form-control eng'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError(message='این ایمیل تکراری است.')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        print(username)
        # if username.startswith('0'):
        #     username = username.replace('0', '+98', 1)
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('شماره‌موبایل تکراری است.')
        return username

    def clean(self):
        cd = super().clean()
        password = cd.get('password')
        confirm_password = cd.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise ValidationError('کلمه عبور و تکرار آن با هم یکی نیستند!')


class UserLoginForm(forms.Form):
    username = PhoneNumberField(label='شماره‌موبایل',  widget=forms.TextInput(
        attrs={'class': 'form-control eng'}), error_messages={
        'invalid': 'فرمت شماره‌موبایل نادرست است. فرمت درست: +989123456789 یا 09123456789'
    })
    password = forms.CharField(label='کلمه عبور', widget=forms.PasswordInput(
        attrs={'class': 'form-control eng'}))
