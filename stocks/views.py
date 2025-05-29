from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test
from stocks.models import Stock 
from sizes.models import Size, SizeQuantity
from number.models import Number, NumberQuantity
from stocks.forms import StockForm, DynamicSizeQuantityForm, DynamicNumberQuantityForm


class StockBaseView(View):
    def get(self, request):
        # Renderiza o template com os dados necessários
        return render(request, 'base.html')
        # Renderiza o template com os dados necessários


@method_decorator(login_required(login_url="login"), name='dispatch')
@method_decorator(user_passes_test(lambda u: u.is_superuser, login_url="login"), name='dispatch')
class StockListView(ListView):
    model = Stock
    template_name = "stock.html"
    context_object_name = "stocks"

    def get_queryset(self):
        # pega o search
        stock = super().get_queryset().order_by('name',)
        search = self.request.GET.get('search')
        if search:
            stock = Stock.objects.filter(name__icontains=search, ).order_by('name', 'collections')
        return stock



@method_decorator(login_required(login_url="login"), name='dispatch')
@method_decorator(user_passes_test(lambda u: u.is_superuser, login_url="stock_list_view"), name='dispatch')
class StockCreateView(CreateView):
    model = Stock
    form_class = StockForm
    template_name = 'stock_create.html'
    success_url = '/stock/'
    
    def get(self, request, *args, **kwargs):
        stock_form = self.form_class()
        size_form = DynamicSizeQuantityForm()
        number_form = DynamicNumberQuantityForm()
        return render(request, self.template_name, {'form': stock_form, 'size_form': size_form, 'number_form': number_form})

    def post(self, request, *args, **kwargs):
        stock_form = self.form_class(request.POST, request.FILES)
        size_form = DynamicSizeQuantityForm(request.POST)
        number_form = DynamicNumberQuantityForm(request.POST)

        if stock_form.is_valid() and size_form.is_valid() and number_form.is_valid():
            stock = stock_form.save()

            for size in Size.objects.all():
                use_size = size_form.cleaned_data.get(f'use_size_{size.id}')
                quantity = size_form.cleaned_data.get(f'quantity_{size.id}')
                if use_size and quantity is not None:
                    SizeQuantity.objects.create(
                        stock=stock,
                        size=size,
                        quantity=quantity
                    )

            for number in Number.objects.all():
                use_number = number_form.cleaned_data.get(f'use_number_{number.id}')
                quantity = number_form.cleaned_data.get(f'quantity_{number.id}')
                if use_number and quantity is not None:
                    NumberQuantity.objects.create(
                        stock=stock,
                        number=number,
                        quantity=quantity
                    )
                    return redirect(self.get_success_url())

        return render(request, self.template_name, {'form': stock_form, 'size_form': size_form, 'number_form': number_form})

    def get_success_url(self):
            action = self.request.POST.get('action')
            if action == 'save_add':
                return reverse_lazy('stock_create_view')  
            else:
                return reverse_lazy('stock_list_view')  


@method_decorator(login_required(login_url="login"), name='dispatch')
@method_decorator(user_passes_test(lambda u: u.is_superuser, login_url="login"), name='dispatch')
class StockUpdateView(UpdateView):
    model = Stock
    form_class = StockForm
    template_name = 'stock_update.html'
    success_url = '/stock/'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        stock_form = self.form_class(instance=self.object)
        size_form = DynamicSizeQuantityForm(stock_instance=self.object)
        number_form = DynamicNumberQuantityForm(stock_instance=self.object)
        return render(request, self.template_name, {'form': stock_form, 'size_form': size_form, 'number_form': number_form})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        stock_form = self.form_class(request.POST, request.FILES, instance=self.object)
        size_form = DynamicSizeQuantityForm(request.POST, stock_instance=self.object)
        number_form = DynamicNumberQuantityForm(request.POST, stock_instance=self.object)
        
        if stock_form.is_valid() and size_form.is_valid() and number_form.is_valid():
            stock = stock_form.save()

            # Limpa e recria os SizeQuantities (ou atualiza)
            for size in Size.objects.all():
                use_size = size_form.cleaned_data.get(f'use_size_{size.id}')
                quantity = size_form.cleaned_data.get(f'quantity_{size.id}')

                if use_size and quantity is not None:
                    sq, created = SizeQuantity.objects.get_or_create(
                        stock=stock,
                        size=size,
                        defaults={'quantity': quantity}
                    )
                    if not created:
                        sq.quantity = quantity
                        sq.save()
                else:
                    # Se estava marcado antes e desmarcou agora, remove
                    SizeQuantity.objects.filter(stock=stock, size=size).delete()
            
            for number in Number.objects.all():
                use_number = number_form.cleaned_data.get(f'use_number_{number.id}')
                quantity = number_form.cleaned_data.get(f'quantity_{number.id}')

                if use_number and quantity is not None:
                    nq, created = NumberQuantity.objects.get_or_create(
                        stock=stock,
                        number=number,
                        defaults={'quantity': quantity}
                    )
                    if not created:
                        nq.quantity = quantity
                        nq.save()
                else:
                    # Se estava marcado antes e desmarcou agora, remove
                    NumberQuantity.objects.filter(stock=stock, number=number).delete()
            return redirect(self.success_url)

        return render(request, self.template_name, {'form': stock_form, 'size_form': size_form})


@method_decorator(login_required(login_url="login"), name='dispatch')
@method_decorator(user_passes_test(lambda u: u.is_superuser, login_url="login"), name='dispatch')
class StockDeleteView(DeleteView):
    model = Stock
    template_name = 'stock_delete.html'
    success_url = '/stock/'


@method_decorator(login_required(login_url="login"), name='dispatch')
@method_decorator(user_passes_test(lambda u: u.is_superuser, login_url="login"), name='dispatch')
class StockDetailView(DetailView):
    model = Stock
    template_name = 'stock_detail.html'
    success_url = '/stock/'
