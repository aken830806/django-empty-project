import datetime
from django import forms


class LoginPostForm(forms.Form):
    username = forms.CharField(max_length=20, initial='')
    pd = forms.CharField(max_length=20, initial='', widget=forms.PasswordInput)
