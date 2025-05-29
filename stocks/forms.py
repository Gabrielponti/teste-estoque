from django import forms
from stocks.models import Stock
from sizes.models import Size, SizeQuantity
from number.models import Number, NumberQuantity


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = "__all__"
        widgets = {
            'collections': forms.CheckboxSelectMultiple(),
            'color': forms.CheckboxSelectMultiple(),
            'images_0': forms.ClearableFileInput(attrs={'class': 'imgs'}),
            'images_1': forms.ClearableFileInput(attrs={'class': 'imgs'}),
            'images_2': forms.ClearableFileInput(attrs={'class': 'imgs'}),
            'images_3': forms.ClearableFileInput(attrs={'class': 'imgs'}),
            'price': forms.TextInput(attrs={'oninput': 'mascaraMoeda(event)'}),
        }
        help_texts = {
            'name': 'Nome do Produto',
            'description': 'Descrição do estoque',
            'image': 'Imagem do estoque',
        }
        error_messages = {
            'name': {
                'max_length': "O nome do estoque é muito longo.",
            },
            'description': {
                'max_length': "A descrição do estoque é muito longa.",
            },
        }
      
    def clean_price(self):
        price = str(self.cleaned_data.get('price'))
        price = price.replace(',', '.') 
        try:
            price = float(price)
        except ValueError:
            raise forms.ValidationError("Preço inválido. Use o formato correto.")
        return price
       
        

class DynamicSizeQuantityForm(forms.Form):
    def __init__(self, *args, stock_instance=None, **kwargs):
        self.stock_instance = stock_instance
        super().__init__(*args, **kwargs)

        sizes = Size.objects.all()
        existing_quantities = {}

        if self.stock_instance:
            # Pega as quantidades existentes relacionadas ao stock
            size_quantities = SizeQuantity.objects.filter(stock=self.stock_instance)
            existing_quantities = {
                sq.size.id: sq.quantity for sq in size_quantities
            }

        for size in sizes:
            self.fields[f'use_size_{size.id}'] = forms.BooleanField(
                label=f"{size.size}",
                required=False,
                initial=(size.id in existing_quantities)
            )
            self.fields[f'quantity_{size.id}'] = forms.IntegerField(
                label="",
                min_value=0,
                required=False,  # Deixar opcional
                # initial=existing_quantities.get(size.id, 0)  # Garantir que tenha valor inicial
            )


class DynamicNumberQuantityForm(forms.Form):
    def __init__(self, *args, stock_instance=None, **kwargs):
        self.stock_instance = stock_instance
        super().__init__(*args, **kwargs)

        numbers = Number.objects.all()
        existing_quantities = {}

        if self.stock_instance:
            # Pega as quantidades existentes relacionadas ao stock
            number_quantities = NumberQuantity.objects.filter(stock=self.stock_instance)
            existing_quantities = {
                nq.number.id: nq.quantity for nq in number_quantities
            }

        for number in numbers:
            self.fields[f'use_number_{number.id}'] = forms.BooleanField(
                label=f"{number.name_number}",
                required=False,
                initial=(number.id in existing_quantities)
            )
            self.fields[f'quantity_{number.id}'] = forms.IntegerField(
                label='',
                min_value=0,
                required=False,  # Deixar opcional
                # initial=existing_quantities.get(number.id, 0)  # Garantir que tenha valor inicial
            )

