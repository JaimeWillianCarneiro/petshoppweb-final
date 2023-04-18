from django import forms

from .models import cliente
class formularioCadastro(forms.ModelForm):
    class Meta:
        model = cliente
        fields = "__all__"
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome:' }), 
            'sobrenome' : forms.TextInput(attrs={'placeholder': 'Sobrenome' }), 
            'email' : forms.TextInput(attrs={'placeholder': 'E-mail' }),
            'sobrenome' : forms.TextInput(attrs={'placeholder': 'Sobrenome' }),
            'nomeUsuario' : forms.TextInput(attrs={'placeholder': 'Nome de usuario' }),
            'cpf' : forms.TextInput(attrs={'placeholder': 'CPF' }),
            'telefone' : forms.TextInput(attrs={'placeholder': 'Telefone' }),
            'senha' : forms.TextInput(attrs={'placeholder': 'senha' }),


            
        }

