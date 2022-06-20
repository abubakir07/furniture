from django import forms
from .models import *


class ContactForm(forms.Form):
    name = forms.CharField(
        min_length = 2,
        widget = forms.TextInput(
            # attr = {'placeholder': 'Ваше имя'}
        )
    )
    email = forms.EmailField(
                widget = forms.EmailInput(
                    # attr = {'placeholder': 'E-mail'}
                )
    )
    message = forms.CharField(
        min_length = 15,
        widget = forms.Textarea(
            # attr = {'placeholder': 'Коментарии', 'cols': 30, 'rows': 9},
        )
    )