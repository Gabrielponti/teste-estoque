from django.forms import ModelForm
from brand.models import Brand


class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
