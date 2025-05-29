from django import forms
from number.models import Number


class NumberModelForm(forms.ModelForm):

    class Meta:
        model = Number
        fields = '__all__'
