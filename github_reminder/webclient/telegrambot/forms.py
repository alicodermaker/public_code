from django import forms
from django.contrib.auth.models import User as User_

from .models import telegramAccount

class ConnectTelegramForm(forms.ModelForm):
    class Meta:
        model = telegramAccount
        fields = ['user', 'id_user', 'first_name', 'last_name']
 
    def __init__(self, *args, **kwargs):
        super(ConnectTelegramForm, self).__init__(*args, **kwargs)


