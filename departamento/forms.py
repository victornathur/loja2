from django.forms import ModelForm, TextInput
from .models import Camisa, Casual

class CamisaForm(ModelForm):
    class Meta:
        model = Camisa
        fields = '__all__'
        widgets = {
            'nome':TextInput(attrs={'class':'form-control'}),
            'dt_nasc':TextInput(attrs={'class':'form-control'}),
            'cpf':TextInput(attrs={'class':'form-control'}),
            'sexo':TextInput(attrs={'class':'form-control'}),

        }

