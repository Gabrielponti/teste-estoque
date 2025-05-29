from django.urls import path
from collection.views import CollectionListView, CollectionUpdateView, CollectionDeleteView


urlpatterns = [
    path('collection/', CollectionListView.as_view(), name='collection_list_view'),
    path('collection/update/<int:pk>/', CollectionUpdateView.as_view(), name='collection_update_view'),
    path('collection/delete/<int:pk>/', CollectionDeleteView.as_view(), name='collection_delete_view'),
]