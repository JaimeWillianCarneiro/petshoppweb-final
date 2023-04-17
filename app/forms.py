from django import forms

from .models import cliente
class formularioCadastro(forms.ModelForm):
    class Meta:
        model = cliente
        fields = "__all__"
