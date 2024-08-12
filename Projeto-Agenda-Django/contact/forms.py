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
        help_text='Texto de ajuda para o nome'
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'class a',
                'placeholder': 'Escreva aqui'
            }
        ),
        label='Sobrenome',
        help_text='Texto de ajuda para o sobrenome'
    )

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'class a',
                'placeholder': 'Digite aqui'
            }
        ),
        label='Telefone',
        help_text='Texto de ajuda para o telefone'
    )
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone', 'email', 'description', 'category'
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
        '''cleaned_data = self.cleaned_data        

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
        
        return super().clean()'''
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Veio do add_error - Não pode ser ABC',
                    code='invalid'
                )
            )

        return first_name