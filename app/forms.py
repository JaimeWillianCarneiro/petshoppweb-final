from django import forms

from .models import cliente

from django.contrib.auth import authenticate, login, logout
# class formularioCadastro(forms.ModelForm):
#     class Meta:
#         model = cliente
#         fields = "__all__"
#         widgets = {
#             'nome': forms.TextInput(attrs={'placeholder': 'Nome:' }), 
#             'sobrenome' : forms.TextInput(attrs={'placeholder': 'Sobrenome' }), 
#             'email' : forms.TextInput(attrs={'placeholder': 'E-mail' }),
#             'sobrenome' : forms.TextInput(attrs={'placeholder': 'Sobrenome' }),
#             'nomeUsuario' : forms.TextInput(attrs={'placeholder': 'Nome de usuario' }),
#             'cpf' : forms.TextInput(attrs={'placeholder': 'CPF' }),
#             'telefone' : forms.TextInput(attrs={'placeholder': 'Telefone' }),
#             'senha' : forms.TextInput(attrs={'placeholder': 'senha' }),


            
#         }



class formularioCadastro(forms.ModelForm):
    class Meta:
        model = cliente
        fields = "__all__"

    def clean_email(self):
        email = self.cleaned_data['email']
        if cliente.objects.filter(email=email).exists():
            raise forms.ValidationError('Esse email já está em uso.')
        return email



# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=100)
#     password = forms.CharField(widget=forms.PasswordInput)
#     def clean(self):
#         cleaned_data = super().clean()
#         username = cleaned_data.get('username')
#         password = cleaned_data.get('password')
#     if not authenticate(username=username, password=password):
#         raise forms.ValidationError('Invalid username or password')


