from django import forms


class formularioCadastro(forms.Form):
    nome = forms.CharField(max_length=50)
    email= forms.EmailField()
    cpf = forms.CharField(max_length=50)
    