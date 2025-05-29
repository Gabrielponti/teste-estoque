from django.forms import ModelForm
from django import forms
from sizes.models import Size


class SizeForm(ModelForm):
    class Meta:
        model = Size
        fields = '__all__'
        labels = {
            'size': 'Tamanho',
        }
        widgets = {
            'size': forms.TextInput(attrs={'placeholder': 'Tamanho'}),
        }
    
    