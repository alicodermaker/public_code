from django import forms
from django.contrib.auth.models import User as User_

from .models import accountCode

class UserVerifyForm(forms.ModelForm):
    class Meta:
        model = accountCode
        fields = ['user']
 
    def __init__(self, *args, **kwargs):
        super(UserVerifyForm, self).__init__(*args, **kwargs)


