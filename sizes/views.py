from django.views import View
from django.views.generic import DeleteView, UpdateView
from django.shortcuts import render, redirect
from sizes.models import Size
from sizes.forms import SizeForm


class SizeListCreateView(View):
    def get(self, request):
        sizes = Size.objects.all().order_by('id')
        form = SizeForm()
        return render(request, 'size_list.html', {'sizes': sizes, 'form': form})

    def post(self, request):
        form = SizeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('size_list_view')
        sizes = Size.objects.all().order_by('id')
        return render(request, 'size_list.html', {'sizes': sizes, 'form': form})


class SizeUpdateView(UpdateView):
    model = Size
    form_class = SizeForm
    template_name = 'size_update.html'
    success_url = "/size/"


class SizeDeleteView(DeleteView):
    model = Size
    success_url = "/size/"
