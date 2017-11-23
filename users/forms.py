# coding=utf-8

from django import forms
from users.utils import validators
from django.forms.utils import ErrorList


__all__ = [
    'LoginForm',
    'DivErrorList',
]


class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''
        return ('<div class="form-error-list">%s</div>' %
                ''.join(['<div class="form-error">%s</div>' % e for e in self]))


class LoginForm(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'validate'}),
        max_length=32,
        min_length=6
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'validate',
                'maxlength': 32,
                'minlength': 8
            }
        ),
    )
    password_length = forms.IntegerField(
        widget=forms.HiddenInput(),
        max_value=32,
        min_value=8
    )
    keep_login = forms.BooleanField(
        widget=forms.CheckboxInput(),
        required=False
    )

    def clean_email(self):
        # Just an example of cleaning a specific filed attribute
        # cleaned_data = super(LoginForm, self).clean()
        # email = cleaned_data.get('email')
        email = self.cleaned_data['email']
        if email == 'test@123.com':
            raise forms.ValidationError
        return email

    # def clean_password_length(self):
    #     password_length = self.cleaned_data['password_length']
    #     if password_length > 32:
    #         raise forms.ValidationError()
    #     elif password_length < 8:
    #         raise forms.ValidationError('')
    #     return password_length
