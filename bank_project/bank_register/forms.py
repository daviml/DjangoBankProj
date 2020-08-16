from django import forms
from .models import Bank

class BankForm(forms.ModelForm):

    class Meta:
        model = Bank
        fields = '__all__'
        labels = {
            'fullname':'Nome',
            'cpf':'CPF',
            'cod':'Código do Banco'
        }
