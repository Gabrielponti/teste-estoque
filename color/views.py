from django.views import View
from django.views.generic import UpdateView, DeleteView
from django.shortcuts import render, redirect
from color.models import Color
from color.forms import ColorForm


class ColorListView(View):
    def get(self, request):
        colors = Color.objects.all().order_by('id')
        form = ColorForm()
        return render(request, 'color_list.html', {'colors': colors, 'form': form})

    def post(self, request):
        form = ColorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('color_list_view')
        colors = Color.objects.all().order_by('id')
        return render(request, 'color_list.html', {'colors': colors, 'form': form})


class ColorUpdateView(UpdateView):
    model = Color
    form_class = ColorForm
    template_name = 'color_update.html'
    success_url = '/color/'  
    success_message = "Cor atualizada com sucesso!"


class ColorDeleteView(DeleteView):
    model = Color
    success_url = "/color/"
    success_message = "Cor deletada com sucesso!"
