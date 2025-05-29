from django.views import View
from django.views.generic import UpdateView, DeleteView
from django.shortcuts import render, redirect
from collection.models import Collection
from collection.forms import CollectionForm


class CollectionListView(View):
    def get(self, request):
        collections = Collection.objects.all().order_by('id')
        form = CollectionForm()
        return render(request, 'collection_list.html', {'collections': collections, 'form': form})

    def post(self, request):
        form = CollectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('collection_list_view')
        collections = Collection.objects.all().order_by('id')
        return render(request, 'collection_list.html', {'collections': collections, 'form': form})


class CollectionUpdateView(UpdateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collection_update.html'
    success_url = '/collection/'  
    success_message = "Coleção atualizada com sucesso!"
    
    
class CollectionDeleteView(DeleteView):
    model = Collection
    success_url = "/collection/"
    success_message = "Coleção deletada com sucesso!"
