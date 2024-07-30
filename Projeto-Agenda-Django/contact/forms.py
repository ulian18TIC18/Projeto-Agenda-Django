from django import forms
from django.core.exceptions import ValidationError

from . import models


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'class a',
                'placeholder': 'Escreva aqui'
            }
        ),
        label='Nome',
        help_text='Texto de ajuda'
    )
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
        )
#        widgets = {
#            'first_name' : forms.TextInput(
#                attrs={
#                    'placeholder': 'Escreva aqui'
#                }
#            ),
#            'last_name' : forms.TextInput(
#                attrs={
#                    'placeholders': 'Escreva aqui'
#                }
#            )
#        }

    def clean(self):
        cleaned_data = self.cleaned_data        

        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )

        self.add_error(
            'last_name',
            ValidationError(
                'Mensagem de erro 2',
                code='invalid'
            )
        )
        
        return super().clean()