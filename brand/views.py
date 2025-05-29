from django.views import View
from django.views.generic import DeleteView, UpdateView
from django.shortcuts import render, redirect
from brand.models import Brand
from brand.forms import BrandForm


class BrandListView(View):
    def get(self, request):
        brands = Brand.objects.all().order_by('id')
        form = BrandForm()
        return render(request, 'brand_list.html', {'brands': brands, 'form': form})

    def post(self, request):
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('brand_list_view')
        brands = Brand.objects.all().order_by('id')
        return render(request, 'brand_list.html', {'brands': brands, 'form': form})


class BrandUpdateView(UpdateView):
    model = Brand
    form_class = BrandForm
    template_name = 'brand_update.html'
    success_url = '/brand/'  
    success_message = "Coleção atualizada com sucesso!"

  
class BrandDeleteView(DeleteView):
    model = Brand
    success_url = '/brand/' 
    success_message = "Coleção deletada com sucesso!"
