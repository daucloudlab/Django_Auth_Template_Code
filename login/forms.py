# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
 
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label="Логин", error_messages={ 'invalid': "Тек әріптер мен сандардан тұрады" })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label="email")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label="Құпия сөз")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label="Құпия сөз (қайтала)")
 
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError("Мұндай қолданушы тіркелген.")
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Құпия сөздер сәйкес келмейді.")
        return self.cleaned_data