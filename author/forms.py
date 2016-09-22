from django import forms

class SigninForm(forms.Form):
        username = forms.CharField(label="Username",
                                   max_length=30,
                                   widget=forms.TextInput(attrs={'class': "form-control input-sm"}))
        password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control input-sm'}))
