from django.views.generic import UpdateView, DeleteView
from django.views import View
from django.shortcuts import render, redirect
from number.models import Number
from number.forms import NumberModelForm


class NumberListView(View):
    def get(self, request):
        numbers = Number.objects.all().order_by('id')
        form = NumberModelForm()
        return render(request, 'number_list.html', {'numbers': numbers, 'form': form})

    def post(self, request):
        form = NumberModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('number_list_view')
        numbers = Number.objects.all().order_by('id')
        return render(request, 'number_list.html', {'numbers': numbers, 'form': form})
    

class NumberUpdateView(UpdateView):
    model = Number
    form_class = NumberModelForm
    template_name = 'number_update.html'
    success_url = '/number/'  
    success_message = "Número atualizado com sucesso!"  


class NumberDeleteView(DeleteView):
    model = Number
    template_name = 'number_delete.html'
    success_url = '/number/' 
