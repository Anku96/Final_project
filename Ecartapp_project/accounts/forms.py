from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder':'Enter password'
        }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder':'Confirm password'
        }))
    
            class Meta:
                model = Account
                fields = ['first_name','last_name','phone_number','email','password']
    
    def __init__(self, *args, **kwargs):
            super(RegistrationForm, self).__init__(*args, **kwargs)
            self.fields['first_name'].widget.attrs['placeholder']='Enter first name'
            self.fields['last_name'].widget.attrs['placeholder']='Enter last name'
            for field in self.fields:
                self.fields[field].widget.attrs['class']='form-control'

