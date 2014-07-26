from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label=u'id ')
    password = forms.CharField(label=u'password ', widget=forms.PasswordInput)
