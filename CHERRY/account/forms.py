from django import forms


class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, label='نام کاربری', widget=forms.TextInput(
        attrs={'class': 'form-control eng'}))
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput(
        attrs={'class': 'form-control eng'}))
    password = forms.CharField(label='کلمه عبور', widget=forms.PasswordInput(
        attrs={'class': 'form-control eng'}))
