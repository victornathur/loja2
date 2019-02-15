from django.forms import ModelForm, TextInput
from .models import Camisa, Casual

class CamisaForm(ModelForm):
    class Meta:
        model = Camisa
        fields = '__all__'
        widgets = {
            'time':TextInput(attrs={'class':'form-control'}),
            'jogador':TextInput(attrs={'class':'form-control'}),
            'numero':TextInput(attrs={'class':'form-control'}),
            'tamanho':TextInput(attrs={'class':'form-control'}),

        }

class CasualForm(ModelForm):
    class Meta:
        model = Casual
        fields = '__all__'
        widgets = {
            'esporte':TextInput(attrs={'class':'form-control'}),
            'cor':TextInput(attrs={'class':'form-control'}),
            'tipo':TextInput(attrs={'class':'form-control'}),
            
        }
