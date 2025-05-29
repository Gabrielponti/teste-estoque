from django.forms import ModelForm
from color.models import Color


class ColorForm(ModelForm):
    class Meta:
        model = Color
        fields = '__all__'
        # mais bonito e legivel 
        # fields = ['name']
